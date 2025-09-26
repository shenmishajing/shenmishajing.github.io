# Website Automation Features

This document describes the automated features implemented for the personal website.

## Resume Download Feature

### Overview
A "Resume" tab has been added to the navigation bar that allows visitors to download the latest PDF version of the resume.

### Implementation
- **Navigation**: Added "Resume" link in `_data/navigation.yml` pointing to `/assets/resume.pdf`
- **Auto-compilation**: GitHub Actions workflow (`.github/workflows/build_resume.yml`) automatically compiles LaTeX resume to PDF
- **Deployment**: PDF is automatically placed in `assets/resume.pdf` and included in the GitHub Pages build

### Triggers
- Manual trigger via GitHub Actions UI
- Automatic trigger when any file in `resume/` directory is modified
- Daily at 2:00 AM UTC to ensure PDF stays updated

### Requirements
- LaTeX environment (handled by GitHub Actions)
- XeLaTeX compiler for font support
- Fonts directory in resume folder

## Multi-Section Synchronization

### Overview
Multiple sections from the LaTeX resume are automatically synchronized to the website using special HTML comments.

### Supported Sections
1. **Publications** (`resume/resume/Publications.tex`) → Publications section
2. **Education** (`resume/resume/Education.tex`) → Education section  
3. **Work Experience** (`resume/resume/Work Experience.tex`) → Work Experience section
4. **Research Experience** (`resume/resume/Research Experience.tex`) → Research Experience section
5. **Awards and Honors** (`resume/resume/Awards and Honors.tex`) → Awards section

### Implementation
- **Special Comments**: Each section uses unique comment markers (e.g., `<!-- AUTO_PUBLICATIONS_START -->`)
- **Parser Script**: `scripts/sync_resume.py` handles multiple LaTeX formats (`cventry`, `cvitemize2`, `cvhonor`)
- **Auto-sync**: GitHub Actions workflow (`.github/workflows/sync_publications.yml`) monitors all sections
- **Format Conversion**: Converts various LaTeX formats to appropriate markdown styles
- **Smart Detection**: Automatically detects which sections have comment blocks and skips missing ones

### Features
- **Multi-Format Support**: Handles different LaTeX environments (`cventries`, `cvitemize2`, `cvhonors`)
- **Nested Brace Handling**: Robust parsing of complex LaTeX with nested braces and special characters
- **Precision Updates**: Only replaces content between special comments, preserving section titles
- **Comment Preservation**: Special comments are preserved for future updates
- **LaTeX Conversion**: Converts LaTeX formatting (bold, italic, math, quotes, links) to markdown
- **Order Preservation**: Maintains content order from resume files

### Triggers
- Manual trigger via GitHub Actions UI
- Automatic trigger when any monitored resume file is modified:
  - `resume/resume/Publications.tex`
  - `resume/resume/Education.tex`
  - `resume/resume/Work Experience.tex`
  - `resume/resume/Research Experience.tex`
  - `resume/resume/Awards and Honors.tex`

## Workflow Details

### Build Resume Workflow
- **File**: `.github/workflows/build_resume.yml`
- **Purpose**: Compiles LaTeX resume and deploys PDF
- **Output**: `assets/resume.pdf`
- **Conflict Handling**: Automatically handles concurrent commits with rebase and retry mechanisms

### Sync Publications Workflow
- **File**: `.github/workflows/sync_publications.yml`
- **Purpose**: Syncs publications from resume to website
- **Output**: Updates `_pages/about.md`
- **Conflict Handling**: Re-runs sync after merges and retries push operations

## Concurrent Execution Handling

### Problem
When both workflows are triggered simultaneously (e.g., when resume files are updated), they may attempt to push changes concurrently, causing Git conflicts.

### Solution
Both workflows implement robust conflict resolution:

1. **Pre-commit Pull**: Pull latest changes before committing
2. **Rebase Strategy**: Use `git pull --rebase` to avoid unnecessary merge commits
3. **Fallback Merge**: If rebase fails, attempt regular merge
4. **Re-sync After Merge**: Publications workflow re-runs the sync script after merge to ensure accuracy
5. **Retry Mechanism**: Up to 3 attempts to push with backoff delays
6. **Automatic Recovery**: If push fails, automatically pull latest changes and retry

### Benefits
- **Zero Manual Intervention**: Conflicts are resolved automatically
- **Data Integrity**: Publications are always re-synced after conflicts to ensure accuracy
- **Reliability**: Multiple retry attempts with exponential backoff
- **Clear Logging**: Detailed error messages for debugging if needed

## Usage

### Updating Resume
1. Edit LaTeX files in `resume/` directory
2. Push changes to main branch
3. GitHub Actions will automatically:
   - Compile new PDF
   - Update website with new resume link
   - Sync publications if Publications.tex was modified

### Manual Triggers
Both workflows can be triggered manually:
1. Go to Actions tab in GitHub repository
2. Select the desired workflow
3. Click "Run workflow"

## File Structure

```
├── .github/workflows/
│   ├── build_resume.yml          # Resume compilation workflow
│   └── sync_publications.yml     # Publications sync workflow
├── assets/
│   └── resume.pdf                # Generated resume PDF
├── resume/
│   ├── resume.tex                # Main resume file
│   └── resume/
│       └── Publications.tex      # Publications section
├── scripts/
│   └── sync_publications.py      # Publications parser script
├── _data/
│   └── navigation.yml            # Updated with Resume link
└── _pages/
    └── about.md                  # Contains synced publications
```

## Maintenance

The system is designed to be low-maintenance. However, if LaTeX format changes significantly, the parser script (`scripts/sync_publications.py`) may need updates to handle new formatting patterns.

## Benefits

1. **Single Source of Truth**: Publications are maintained only in the resume LaTeX file
2. **Consistency**: Website always shows the latest resume and publications
3. **Automation**: No manual copying or format conversion required
4. **Professional**: Resume is always professionally formatted via LaTeX
5. **Accessibility**: Resume is easily downloadable from the website
