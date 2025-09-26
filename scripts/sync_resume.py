#!/usr/bin/env python3
"""
Script to sync multiple sections from LaTeX resume to Jekyll markdown
"""

import os
import re
import sys

# Configuration for different sections
SECTIONS_CONFIG = {
    "publications": {
        "latex_file": "resume/resume/Publications.tex",
        "comment_start": "<!-- AUTO_PUBLICATIONS_START -->",
        "comment_end": "<!-- AUTO_PUBLICATIONS_END -->",
        "parser_type": "cvitemize2",
    },
    "education": {
        "latex_file": "resume/resume/Education.tex",
        "comment_start": "<!-- AUTO_EDUCATION_START -->",
        "comment_end": "<!-- AUTO_EDUCATION_END -->",
        "parser_type": "cventry",
    },
    "work_experience": {
        "latex_file": "resume/resume/Work Experience.tex",
        "comment_start": "<!-- AUTO_WORK_EXPERIENCE_START -->",
        "comment_end": "<!-- AUTO_WORK_EXPERIENCE_END -->",
        "parser_type": "cventry",
    },
    "research_experience": {
        "latex_file": "resume/resume/Research Experience.tex",
        "comment_start": "<!-- AUTO_RESEARCH_EXPERIENCE_START -->",
        "comment_end": "<!-- AUTO_RESEARCH_EXPERIENCE_END -->",
        "parser_type": "cventry",
    },
    "awards": {
        "latex_file": "resume/resume/Awards and Honors.tex",
        "comment_start": "<!-- AUTO_AWARDS_START -->",
        "comment_end": "<!-- AUTO_AWARDS_END -->",
        "parser_type": "cvhonor",
    },
}


def read_latex_file(latex_file):
    """Read LaTeX file content"""
    try:
        with open(latex_file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: LaTeX file {latex_file} not found")
        return None


def parse_cvitemize2_section(content):
    """Parse publications section with cvitemize2 format"""
    # Look for \item statements within the cvitemize2 environment
    items_pattern = r"\\item\s+(.*?)(?=\\item|\\vspace|\\end\{cvitemize2\})"
    items = re.findall(items_pattern, content, re.DOTALL)

    parsed_items = []
    for item in items:
        # Clean up the item text
        cleaned_item = item.strip()
        if cleaned_item and not cleaned_item.startswith(
            "%"
        ):  # Skip comments and empty items
            # Remove trailing % symbols and anything after them (LaTeX comments)
            cleaned_item = re.sub(r"\s*%.*$", "", cleaned_item, flags=re.MULTILINE)
            parsed_items.append(cleaned_item)

    return parsed_items


def parse_cventry_section(content):
    """Parse education/experience sections with cventry format"""
    # Find all \cventry commands
    cventry_starts = []
    for match in re.finditer(r"\\cventry\s*", content):
        cventry_starts.append(match.end())

    entries = []
    for start_pos in cventry_starts:
        # Extract 5 parameters from the cventry command
        params = []
        pos = start_pos

        for param_num in range(
            5
        ):  # Extract 5 parameters: {position}{title}{location}{date}{description}
            # Skip whitespace, comments, and other characters until we find opening brace
            while pos < len(content):
                if content[pos] == "{":
                    break
                elif content[pos] == "%":
                    # Skip comment line
                    while pos < len(content) and content[pos] != "\n":
                        pos += 1
                elif content[pos] in " \t\n":
                    pos += 1
                else:
                    pos += 1  # Skip other characters

            if pos >= len(content) or content[pos] != "{":
                break  # No more parameters

            # Extract content between matching braces
            brace_count = 1
            start_brace = pos + 1
            pos += 1

            while pos < len(content) and brace_count > 0:
                if content[pos] == "{":
                    brace_count += 1
                elif content[pos] == "}":
                    brace_count -= 1
                pos += 1

            if brace_count == 0:
                param_content = content[start_brace : pos - 1]
                params.append(param_content)
            else:
                break  # Unmatched braces

        if len(params) == 5:
            entries.append(tuple(params))

    parsed_items = []
    for entry in entries:
        position, title, location, date, description = entry

        # Clean up each field
        position = position.strip()
        title = title.strip()
        location = location.strip()
        date = date.strip()
        description = description.strip()

        # Skip entries with empty title and description
        if not title and not description:
            continue

        parsed_items.append(
            {
                "position": position,
                "title": title,
                "location": location,
                "date": date,
                "description": description,
            }
        )

    return parsed_items


def parse_cvhonor_section(content):
    """Parse awards section with cvhonor format"""
    # Use a more robust approach to handle nested braces
    # First find all cvhonor lines (excluding comments)
    lines = content.split("\n")
    cvhonor_lines = []
    for line in lines:
        if line.strip().startswith("\\cvhonor") and not line.strip().startswith("%"):
            cvhonor_lines.append(line.strip())

    parsed_items = []
    for line in cvhonor_lines:
        # Extract parameters by finding matching braces
        params = []
        i = line.find("{")
        while i != -1 and len(params) < 3:
            # Find matching closing brace
            brace_count = 1
            j = i + 1
            while j < len(line) and brace_count > 0:
                if line[j] == "{":
                    brace_count += 1
                elif line[j] == "}":
                    brace_count -= 1
                j += 1

            if brace_count == 0:
                params.append(line[i + 1 : j - 1])
                # Find next opening brace
                i = line.find("{", j)
            else:
                break

        if len(params) == 3:
            award_type, institution, date = params

            # Clean up each field
            award_type = award_type.strip()
            institution = institution.strip()
            date = date.strip()

            # Skip empty entries
            if not award_type.strip():
                continue

            parsed_items.append(
                {"award_type": award_type, "institution": institution, "date": date}
            )

    return parsed_items


def convert_latex_to_markdown(latex_text):
    """Convert LaTeX formatting to markdown"""
    text = latex_text

    # Convert textbf to markdown bold
    text = re.sub(r"\\textbf\{([^}]+)\}", r"**\1**", text)

    # Convert textit to markdown italic for conference names using underscores
    text = re.sub(r"\\textit\{([^}]+)\}", r"_\1_", text)

    # Convert href to markdown links
    text = re.sub(
        r"\\href\{([^}]+)\}\{\\textcolor\{link\}\{([^}]+)\}\}", r"[\2](\1)", text
    )

    # Convert textcolor to simple text (removing color formatting)
    text = re.sub(r"\\textcolor\{[^}]+\}\{([^}]+)\}", r"\1", text)

    # Handle LaTeX quotes - convert to proper double quotes
    # Use non-greedy matching and handle quotes that may contain apostrophes
    text = re.sub(r"``(.*?)\'\'", r'"\1"', text)

    # Preserve LaTeX math for superscripts (keep $ signs for proper rendering)
    # Don't convert these - keep them as LaTeX for proper markdown math rendering
    # text = re.sub(r"\$\^\\text\{([^}]+)\}\$", r"$^\{\\text\{\1\}\}$", text)

    # Handle specific LaTeX math superscripts that need to be preserved
    text = re.sub(r"\$\^\\text\{([^}]+)\}\$", r"$^\\text{\1}$", text)
    # Keep other math expressions intact
    # text = re.sub(r"\$\^([^$]+)\$", r"$^\1$", text)

    # Remove LaTeX commands that don't have direct markdown equivalents
    text = re.sub(r"\\vspace\{[^}]+\}", "", text)
    text = re.sub(r"\\qquad\\?", "", text)
    text = re.sub(r"\\text\{([^}]+)\}", r"\\text{\1}", text)  # Keep \text for math mode

    # Remove remaining LaTeX commands but preserve math expressions
    # Don't remove content within $ signs
    parts = re.split(r"(\$[^$]*\$)", text)
    for i in range(0, len(parts), 2):  # Process non-math parts only
        # Remove LaTeX commands but keep their content if meaningful
        parts[i] = re.sub(r"\\([a-zA-Z]+)\{([^}]*)\}", r"\2", parts[i])
        parts[i] = re.sub(
            r"\\([a-zA-Z]+)\s*", "", parts[i]
        )  # Remove commands without parameters
        # Clean up remaining LaTeX artifacts from non-math parts only
        parts[i] = parts[i].replace("{", "").replace("}", "")

    text = "".join(parts)

    # Clean up whitespace
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


def generate_publications_markdown(publications):
    """Generate markdown for publications list"""
    markdown_lines = []
    for pub in publications:
        converted_pub = convert_latex_to_markdown(pub)
        markdown_lines.append(f"- {converted_pub}")
    return "\n".join(markdown_lines)


def generate_education_markdown(education_entries):
    """Generate markdown for education section"""
    markdown_lines = []

    for entry in education_entries:
        date = entry["date"]
        title = convert_latex_to_markdown(entry["title"])
        location = convert_latex_to_markdown(entry["location"])
        institution = convert_latex_to_markdown(entry["position"])
        # Skip description for education - only show date, degree, institution, location

        # Format: - date, title, institution, location (no description, no italic date)
        line_parts = []
        if date:
            line_parts.append(date)
        if title:
            line_parts.append(title)
        if institution:
            line_parts.append(institution)
        if location and location != institution:  # Avoid duplicate location info
            line_parts.append(location)

        line = f"- {', '.join(line_parts)}"
        markdown_lines.append(line)

    return "\n".join(markdown_lines)


def generate_experience_markdown(experience_entries, experience_type="experience"):
    """Generate markdown for work/research experience sections"""
    markdown_lines = []

    for entry in experience_entries:
        date = entry["date"]
        title = convert_latex_to_markdown(entry["title"])
        location = convert_latex_to_markdown(entry["location"])
        position = convert_latex_to_markdown(entry["position"])
        description = entry["description"] if entry["description"] else ""

        # Create entry header
        header_parts = []
        if title:
            header_parts.append(f"**{title}**")
        if location:
            header_parts.append(location)
        if date:
            header_parts.append(f"*({date})*")

        if header_parts:
            markdown_lines.append(f"- {' - '.join(header_parts)}")

            # Add description if available
            if description:
                # Parse bullet points from description
                # Look for \item statements within cvitems environment
                item_pattern = r"\\item\s+(.*?)(?=\s*\\item|\s*\\end|$)"
                items = re.findall(item_pattern, description, re.DOTALL)

                for item in items:
                    # Convert LaTeX formatting to markdown for each item
                    item_clean = convert_latex_to_markdown(item.strip())
                    if item_clean:
                        markdown_lines.append(f"  - {item_clean}")

            markdown_lines.append("")  # Add blank line between entries

    return "\n".join(markdown_lines).rstrip()  # Remove trailing blank line


def generate_awards_markdown(awards_entries):
    """Generate markdown for awards and honors section"""
    markdown_lines = []

    for entry in awards_entries:
        award_type = convert_latex_to_markdown(entry["award_type"])
        institution = convert_latex_to_markdown(entry["institution"])
        date = entry["date"].replace("\\qquad\\", "").strip()

        # Extract date in readable format
        date_match = re.search(r"([A-Z][a-z]{2}\.\s*\d{4})", date)
        if date_match:
            formatted_date = date_match.group(1).replace(".", "")
        else:
            formatted_date = date

        # Format line
        line_parts = []
        if formatted_date:
            line_parts.append(f"*{formatted_date}*")

        # Award type is already converted by convert_latex_to_markdown
        line_parts.append(award_type)

        if institution:
            line_parts.append(institution)

        markdown_lines.append(f"- {', '.join(line_parts)}")

    return "\n".join(markdown_lines)


def update_about_md_section(section_name, markdown_content):
    """Update a specific section in about.md using special comments"""
    about_file = "_pages/about.md"
    config = SECTIONS_CONFIG[section_name]

    try:
        with open(about_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {about_file} not found")
        return False

    # Find the special comment boundaries
    start_pattern = re.escape(config["comment_start"])
    end_pattern = re.escape(config["comment_end"])

    start_match = re.search(start_pattern, content)
    end_match = re.search(end_pattern, content)

    if not start_match or not end_match:
        print(f"Error: Could not find {section_name} comment boundaries in about.md")
        print(
            f"Please ensure the file contains {config['comment_start']} and {config['comment_end']} comments"
        )
        return False

    # Replace only the content between the comments, preserving the comments themselves
    before_section = content[: start_match.end()]
    after_section = content[end_match.start() :]

    # Add the new content with proper spacing
    new_content = before_section + "\n" + markdown_content + "\n" + after_section

    # Write the updated content
    try:
        with open(about_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully updated {section_name} in about.md")
        return True
    except Exception as e:
        print(f"Error writing to {about_file}: {e}")
        return False


def check_comment_blocks_exist(section_name):
    """Check if the special comment blocks exist in about.md for the given section"""
    about_file = "_pages/about.md"
    config = SECTIONS_CONFIG[section_name]

    try:
        with open(about_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {about_file} not found")
        return False

    start_comment = config["comment_start"]
    end_comment = config["comment_end"]

    has_start = start_comment in content
    has_end = end_comment in content

    if not has_start or not has_end:
        print(f"Warning: Comment blocks for {section_name} not found in about.md")
        if not has_start:
            print(f"  Missing: {start_comment}")
        if not has_end:
            print(f"  Missing: {end_comment}")
        return False

    return True


def sync_section(section_name):
    """Sync a specific section from LaTeX to markdown"""
    config = SECTIONS_CONFIG[section_name]
    latex_file = config["latex_file"]
    parser_type = config["parser_type"]

    print(f"Reading {section_name} from {latex_file}")

    # Read LaTeX file
    content = read_latex_file(latex_file)
    if content is None:
        return False

    # Parse based on section type
    if parser_type == "cvitemize2":
        parsed_items = parse_cvitemize2_section(content)
        markdown_content = generate_publications_markdown(parsed_items)
    elif parser_type == "cventry":
        parsed_items = parse_cventry_section(content)
        if section_name == "education":
            markdown_content = generate_education_markdown(parsed_items)
        else:  # work_experience or research_experience
            markdown_content = generate_experience_markdown(parsed_items, section_name)
    elif parser_type == "cvhonor":
        parsed_items = parse_cvhonor_section(content)
        markdown_content = generate_awards_markdown(parsed_items)
    else:
        print(f"Error: Unknown parser type {parser_type} for section {section_name}")
        return False

    if not parsed_items:
        print(f"No {section_name} entries found in LaTeX file")
        return False

    print(f"Found {len(parsed_items)} {section_name} entries")

    # Update about.md
    return update_about_md_section(section_name, markdown_content)


def main():
    """Main function"""
    # Change to the repository root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    os.chdir(repo_root)

    # Get sections to sync from command line arguments
    import sys

    if len(sys.argv) > 1:
        sections_to_sync = [arg for arg in sys.argv[1:] if arg in SECTIONS_CONFIG]
    else:
        # Default: sync all sections
        sections_to_sync = list(SECTIONS_CONFIG.keys())

    print(f"Syncing sections: {', '.join(sections_to_sync)}")

    success_count = 0
    skipped_count = 0
    total_count = len(sections_to_sync)

    for section_name in sections_to_sync:
        print(f"\n--- Syncing {section_name} ---")

        # First check if this section has comment blocks
        if not check_comment_blocks_exist(section_name):
            print(f"Skipped {section_name} - comment blocks not found in about.md")
            skipped_count += 1
            continue

        if sync_section(section_name):
            success_count += 1
        else:
            print(f"Failed to sync {section_name}")

    attempted_count = total_count - skipped_count
    print("\n=== Summary ===")
    print(f"Total sections: {total_count}")
    print(f"Skipped sections: {skipped_count}")
    print(f"Successfully synced: {success_count}/{attempted_count}")

    if attempted_count == 0:
        print("No sections were processed (all skipped)")
        return 0
    elif success_count == attempted_count:
        print("All attempted sections synced successfully!")
        return 0
    else:
        print("Some sections failed to sync")
        return 1


if __name__ == "__main__":
    sys.exit(main())
