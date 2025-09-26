import json
import os
import signal
import sys
import time
from datetime import datetime
from typing import Any, Dict

import requests
from requests.adapters import HTTPAdapter
from scholarly import scholarly
from urllib3.util.retry import Retry


def timeout_handler(signum, frame):
    """Handle timeout signal"""
    raise TimeoutError("Google Scholar request timed out")


def configure_scholarly_session():
    """Configure scholarly library with timeout and retry settings"""
    try:
        # Configure requests session with timeout and retries
        session = requests.Session()

        # Set up retry strategy
        retry_strategy = Retry(
            total=3,  # Total number of retries
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry
            backoff_factor=2,  # Wait time between retries (exponential backoff)
            raise_on_status=False,
        )

        # Create adapter with retry strategy
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Set timeout for all requests
        session.timeout = 30  # 30 seconds per request

        # Configure scholarly to use this session
        scholarly.set_timeout(30)
        print("✅ Scholarly session configured with timeout and retry settings")

    except Exception as e:
        print(f"⚠️  Warning: Could not configure scholarly session: {e}")
        print("Proceeding with default settings...")


def scrape_with_timeout(timeout_seconds: int = 300) -> Dict[Any, Any]:
    """Scrape Google Scholar data with timeout protection"""
    # Set up signal handler for timeout
    signal.signal(signal.SIGALRM, timeout_handler)

    try:
        # Set timeout
        signal.alarm(timeout_seconds)

        print(
            f"Starting to scrape Google Scholar for user: {os.environ['GOOGLE_SCHOLAR_ID']}"
        )
        print(f"Timeout set to {timeout_seconds} seconds")

        # Search for author
        print("Step 1: Searching for author...")
        signal.alarm(120)  # 2 minutes for author search
        author: dict = scholarly.search_author_id(os.environ["GOOGLE_SCHOLAR_ID"])
        print("Author found successfully")

        # Fill author information
        print("Step 2: Filling author information...")
        signal.alarm(timeout_seconds - 120)  # Remaining time for filling data
        scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
        print("Author information filled successfully")

        # Cancel timeout
        signal.alarm(0)
        return author

    except TimeoutError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        # Make sure to cancel any pending alarm
        signal.alarm(0)


# Configure scholarly library
configure_scholarly_session()

# Main execution with timeout protection and retry logic
MAX_ATTEMPTS = 3
TIMEOUT_SECONDS = int(
    os.environ.get("SCHOLAR_TIMEOUT", "600") or "600"
)  # Default 10 minutes
print(f"🔧 Timeout configured: {TIMEOUT_SECONDS} seconds")

author = None
for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        print(f"\n🔄 Attempt {attempt}/{MAX_ATTEMPTS} to scrape Google Scholar data")
        author = scrape_with_timeout(TIMEOUT_SECONDS)
        print("✅ Data scraping completed successfully!")
        break
    except (TimeoutError, Exception) as e:
        print(f"❌ Attempt {attempt} failed: {e}")
        if attempt < MAX_ATTEMPTS:
            wait_time = min(
                60 * attempt, 300
            )  # Progressive wait: 60s, 120s, then max 5min
            print(f"⏳ Waiting {wait_time} seconds before retry...")
            time.sleep(wait_time)
        else:
            print("🚨 All attempts to scrape Google Scholar data have failed.")
            print(f"🚨 Final error: {e}")
            print("⚠️  Continuing without Google Scholar data...")

# Graceful handling when scraping fails
if author is None:
    print("⚠️  Google Scholar data could not be retrieved after all attempts.")
    print("📝 Creating placeholder data files to prevent workflow failure...")

    # Create minimal placeholder data
    placeholder_author = {
        "name": "Unknown",
        "updated": str(datetime.now()),
        "publications": {},
        "citedby": 0,
        "error": "Failed to scrape Google Scholar data",
    }

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as outfile:
        json.dump(placeholder_author, outfile, ensure_ascii=False)

    placeholder_shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": "N/A",
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(placeholder_shieldio_data, outfile, ensure_ascii=False)

    print("✅ Placeholder files created. Workflow can continue.")
    print("💡 Check your GOOGLE_SCHOLAR_ID and SCHOLAR_TIMEOUT settings.")
else:
    # Process and save the scraped data successfully
    print("📊 Processing scraped data...")
    name = author["name"]
    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}
    print(f"📈 Found {len(author['publications'])} publications for {name}")
    print(json.dumps(author, indent=2))

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    print("✅ Google Scholar data saved successfully!")

print("🏁 Script completed. Check results/ directory for output files.")
