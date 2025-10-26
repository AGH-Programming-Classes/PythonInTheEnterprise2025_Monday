#!/usr/bin/env python3
"""
CLI entrypoint for the Quote Scraper project.

Commands:
  - fetch : download quotes from the website and save them (json/csv)
  - stats : analyze a JSON file with quotes and print simple statistics
"""
import argparse
import json
import csv
from pathlib import Path
from collections import Counter
from typing import List

import fetch
import parse
from models import Quote
from strategies import StrategyFactory


# ---------------- Command: fetch ----------------
def cmd_fetch(args: argparse.Namespace) -> None:
    """
    CLI command: fetch
    Crawl the quotes site, parse quotes and save them using the selected strategy (json/csv).
    """
    print(f"[INFO] Starting crawl: pages={args.pages}, tag={args.tag}, delay={args.delay}s")

    html_pages: List[str] = fetch.crawl_quotes(pages=args.pages, tag=args.tag, delay=args.delay)
    all_quotes: List[Quote] = []

    for i, html in enumerate(html_pages, start=1):
        quotes = parse.parse_quotes(html)
        print(f"[INFO] Page {i}: found {len(quotes)} quotes.")
        all_quotes.extend(quotes)

    output_path = Path(args.out)

    # Choose a saving strategy via factory
    try:
        strategy = StrategyFactory.get(args.format)
    except ValueError as e:
        print(f"[ERROR] {e}")
        return

    # Save using the selected strategy
    strategy.save(all_quotes, output_path)


# ---------------- Command: stats ----------------
def cmd_stats(args: argparse.Namespace) -> None:
    """
    CLI command: stats
    Analyze a JSON file with quotes and print summary statistics.
    """
    src_path = Path(args.src)
    if not src_path.exists():
        print(f"[ERROR] File {src_path} does not exist.")
        return

    # Load JSON data
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse JSON: {e}")
        return

    # Collect authors and tags
    authors = [q.get("author", "") for q in data]
    tags = [t for q in data for t in q.get("tags", [])]

    author_counts = Counter(authors)
    tag_counts = Counter(tags)

    print("\n Most popular authors:")
    for author, count in author_counts.most_common(args.top):
        print(f"  {author:<25} — {count} quotes")

    print("\n Most frequent tags:")
    for tag, count in tag_counts.most_common(args.top):
        print(f"  {tag:<20} — {count} occurrences")

    print("\n[DONE] Analysis finished.")


# ---------------- Main parser ----------------
def main() -> None:
    parser = argparse.ArgumentParser(prog="quote-scraper", description="CLI for scraping and analyzing quotes.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # fetch subcommand
    fetch_parser = subparsers.add_parser("fetch", help="Download quotes from the website.")
    fetch_parser.add_argument("--pages", type=int, default=1, help="Number of pages to crawl (default: 1).")
    fetch_parser.add_argument("--tag", type=str, default=None, help="Tag to filter quotes (e.g. love, life).")
    fetch_parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests in seconds.")
    fetch_parser.add_argument("--out", type=str, default="data/quotes.json", help="Output file path.")
    fetch_parser.add_argument("--format", type=str, choices=["json", "csv"], default="json", help="Output format.")
    fetch_parser.set_defaults(func=cmd_fetch)

    # stats subcommand
    stats_parser = subparsers.add_parser("stats", help="Analyze statistics from a JSON file with quotes.")
    stats_parser.add_argument("--src", type=str, required=True, help="Path to the JSON file with quotes.")
    stats_parser.add_argument("--top", type=int, default=5, help="Number of top items to display.")
    stats_parser.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    args.func(args)


if _name_ == "_main_":
    main()