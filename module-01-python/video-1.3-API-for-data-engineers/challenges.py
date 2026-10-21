"""Video 1.3 homework — three API engineering challenges.

Run from the repo root: python exercises/03_api_exercises.py
Do them, commit, and push. Solutions go up 24 hours after the video.
"""

from pathlib import Path
import os
import time
import requests
from dotenv import load_dotenv

BASE_URL = "https://jsonplaceholder.typicode.com"

# ---------------------------------------------------------------
# CHALLENGE 1: Safe Request with Timeout & Error Raising
# Write a function `fetch_user(user_id: int) -> dict` that:
# 1. Calls GET {BASE_URL}/users/{user_id} with a 5-second timeout.
# 2. Calls raise_for_status() to catch bad responses.
# 3. Returns the JSON response as a dictionary.
# Test it with user_id=1 (should return user dict) and user_id=999 (should raise HTTPError).
# ---------------------------------------------------------------
def fetch_user(user_id: int) -> dict:
    # TODO
    pass


# ---------------------------------------------------------------
# CHALLENGE 2: Page-Based Pagination with Safeguards
# Write a function `fetch_comments(max_pages: int = 5) -> list` that:
# 1. Loops through pages starting at page 1 using GET {BASE_URL}/comments
#    with query params `_page` and `_limit=20`.
# 2. Stops early if an empty list is returned.
# 3. Accumulates all comment objects into a single flat list using .extend().
# 4. Sleeps 0.5 seconds between page calls to remain polite.
# Expected output when max_pages=5: 100 total comments collected across 5 pages.
# ---------------------------------------------------------------
def fetch_comments(max_pages: int = 5) -> list:
    # TODO
    pass


# ---------------------------------------------------------------
# CHALLENGE 3: Retries with Exponential Backoff (The Wi-Fi Challenge)
# Write a function `fetch_with_retry(url: str, max_retries: int = 3) -> dict` that:
# 1. Attempts to GET the provided URL (timeout 5s).
# 2. Uses a try/except block capturing `requests.RequestException`.
# 3. On failure, prints the attempt number and error, then sleeps for 2 ** attempt seconds.
# 4. On the 3rd failed attempt (attempt == max_retries - 1), re-raises the exception loudly.
# 5. On success, breaks out of the retry loop and returns response.json().
# 
# TEST IT: Run your code, disconnect your Wi-Fi/internet mid-run, and verify that 
# it logs all 3 attempts with exponential backoff before failing loudly!
# ---------------------------------------------------------------
def fetch_with_retry(url: str, max_retries: int = 3) -> dict:
    # TODO
    pass


if __name__ == "__main__":
    print("--- Testing Challenge 1 ---")
    # user = fetch_user(1)
    # print(f"Fetched user: {user.get('name')}")

    print("\n--- Testing Challenge 2 ---")
    # comments = fetch_comments(max_pages=5)
    # print(f"Total comments fetched: {len(comments)}")

    print("\n--- Testing Challenge 3 ---")
    # data = fetch_with_retry(f"{BASE_URL}/posts/1")
    # print(f"Fetched post title: {data.get('title')}")