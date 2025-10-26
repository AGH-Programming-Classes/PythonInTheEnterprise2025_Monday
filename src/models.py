"""
Domain models used by the project.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Quote:
    """
    Represents a single quote scraped from quotes.toscrape.com
    """
    text: str
    author: str
    tags: List[str]