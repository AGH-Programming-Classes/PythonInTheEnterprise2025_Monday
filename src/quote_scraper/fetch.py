"""
Fetching / crawling utilities for quotes.toscrape.com
"""
import time
from typing import Optional, List
import requests

BASE_URL = "https://quotes.toscrape.com"


def fetch_page(url: str) -> Optional[str]:
    """
    Fetch HTML content of the given URL.
    Returns the HTML text, or None if an error occurred.
    """
    headers = {
        "User-Agent": "QuoteScraperBot/1.0 (+https://github.com/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        print(f"[HTTP ERROR] {e} -> {url}")
    except requests.exceptions.RequestException as e:
        print(f"[REQUEST ERROR] {e} -> {url}")
    return None


def crawl_quotes(pages: int = 1, tag: Optional[str] = None, delay: float = 0.5) -> List[str]:
    """
    Crawl the quotes website, returning a list of HTML pages (one per page crawled).

    :param pages: number of pages to fetch
    :param tag: optional tag filter (e.g. "love", "life")
    :param delay: delay between requests in seconds
    :return: list of HTML page contents (str)
    """
    html_pages: List[str] = []

    for page in range(1, pages + 1):
        if tag:
            url = f"{BASE_URL}/tag/{tag}/page/{page}/"
        else:
            url = f"{BASE_URL}/page/{page}/"

        print(f"[INFO] Fetching page {page} -> {url}")
        html = fetch_page(url)

        if html is None:
            print(f"[WARN] Skipping page {page} (no data).")
            break

        # If the website signals no quotes or 404, stop crawling further pages.
        if "No quotes found!" in html or "404" in html:
            print(f"[INFO] No more pages (404 or empty) — stopping.")
            break

        html_pages.append(html)
        time.sleep(delay)

    print(f"[DONE] Fetching finished. Pages fetched: {len(html_pages)}")
    return html_pages