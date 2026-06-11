"""
Google Ads Transparency API: A Quick Start Example
See more at: https://apify.com/johnvc/google-ads-transparency-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-ads-transparency-api/input-schema?fpr=9n7kx3

This script shows how to call the Google Ads Transparency API on Apify from
Python and read its structured JSON output. It lists an advertiser's ads from
the Google Ads Transparency Center. Inputs are kept small so your first call
stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one advertiser, 20 ads) to keep this first run
# inexpensive: you are billed per ad returned. The advertiser ID is the AR...
# code in a Google Ads Transparency Center advertiser URL.
run_input = {
    "advertiserId": "AR01614014350098432001",
    "maxResultsPerAdvertiser": 20,
    # "region": "...",  # optional Google ads region code; leave out for ads shown anywhere
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-ads-transparency-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} ad(s).\n")

# Show each ad with its format and how long it has run.
for item in items:
    advertiser = item.get("advertiser", "")
    fmt = item.get("format", "")
    days = item.get("total_days_shown")
    link = item.get("link", "")
    print(f"{item.get('position')}. {advertiser} [{fmt}] run {days} day(s)")
    print(f"   {link}\n")
