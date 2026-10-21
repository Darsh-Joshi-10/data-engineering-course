import time
import requests

BASE = "https://jsonplaceholder.typicode.com"

def fetch_all_posts(max_pages: int = 4, sleep_seconds: float = 0) -> list:
    """Page-based pagination: loop pages, accumulate, stop when empty."""
    all_posts = []

    for page in range(1, max_pages + 1):
        for attempt in range(3):
            try:
                r = requests.get(
                    f"{BASE}/posts",
                    params={"_page": page, "_limit": 10},
                    timeout=10,
                )
                r.raise_for_status()
                break  # success — leave the retry loop
            except requests.RequestException as e:
                print(f"Page {page}, attempt {attempt + 1} failed: {e}")
                if attempt == 2:
                    raise  # 3rd failure — give up loudly
                time.sleep(2 ** attempt)  # backoff: 1s, 2s

    return all_posts

fetch_all_posts()