"""
Google Ads Transparency API: Batch Multi-Advertiser Example
See more at: https://apify.com/johnvc/google-ads-transparency-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-ads-transparency-api/input-schema?fpr=9n7kx3

This script shows the batch capability of the Google Ads Transparency API on
Apify: pass a list of advertiser IDs with the `advertiserIds` input and the
Actor pulls each ad library in a single run, tagging every ad with its
`advertiser_id`. That makes it easy to compare competitors' ad activity side by
side. Inputs are kept small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from collections import defaultdict
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# This run uses the `advertiserIds` list to pull several ad libraries at once.
# Each ad row carries the `advertiser_id` it came from. maxResultsPerAdvertiser
# is kept small (10) to keep this first run inexpensive: you are billed per ad
# returned. Raise it or add advertisers once you know your budget.
run_input = {
    "advertiserIds": ["AR01614014350098432001", "AR13614460755715375105"],
    "maxResultsPerAdvertiser": 10,   # small on purpose to keep it cheap
    # "region": "...",               # optional Google ads region code; leave out for ads shown anywhere
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-ads-transparency-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} ad(s) across {len(run_input['advertiserIds'])} advertiser(s).\n")

# Group the ads by their advertiser so the batch structure is visible.
by_advertiser = defaultdict(list)
for item in items:
    by_advertiser[item.get("advertiser_id", "")].append(item)

# Print a short report per advertiser.
for advertiser_id in run_input["advertiserIds"]:
    ads = by_advertiser.get(advertiser_id, [])
    name = ads[0].get("advertiser", advertiser_id) if ads else advertiser_id
    print(f"=== {name} ({advertiser_id}): {len(ads)} ad(s) ===")
    for item in ads:
        fmt = item.get("format", "")
        days = item.get("total_days_shown")
        print(f"  {item.get('position')}. [{fmt}] run {days} day(s)  {item.get('link', '')}")
    print()
