"""
HTML parsing utilities to extract Quote objects from a page's HTML.
"""
from bs4 import BeautifulSoup
from typing import List
from models import Quote


def parse_quotes(html: str) -> List[Quote]:
    """
    Parse quotes from the provided HTML and return a list of Quote dataclass instances.

    :param html: HTML page content as a string
    :return: list of Quote objects
    """
    soup = BeautifulSoup(html, "html.parser")
    quote_divs = soup.select("div.quote")

    quotes: List[Quote] = []

    for div in quote_divs:
        text_elem = div.select_one("span.text")
        author_elem = div.select_one("small.author")
        tag_elems = div.select("div.tags a.tag")

        text = text_elem.get_text(strip=True) if text_elem else ""
        author = author_elem.get_text(strip=True) if author_elem else ""
        tags = [t.get_text(strip=True) for t in tag_elems]

        quotes.append(Quote(text=text, author=author, tags=tags))

    return quotes