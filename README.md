# Quote Scraper

A command-line web scraper for `quotes.toscrape.com`. This tool allows you to fetch quotes from the website, save them in various formats (JSON or CSV), and analyze the collected data.

## Features

*   **Fetch quotes:** Crawl the website and download quotes.
*   **Filter by tag:** Scrape quotes belonging to a specific tag (e.g., "love", "life").
*   **Multiple pages:** Scrape quotes from multiple pages.
*   **Save in different formats:** Save the scraped quotes as JSON or CSV files.
*   **Analyze quotes:** Get statistics on the most popular authors and tags from a JSON file.
*   **Configurable delay:** Set a delay between HTTP requests to avoid overloading the server.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/quote-scraper.git
    cd quote-scraper
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The command-line interface (CLI) is the main entry point for using the scraper. It has two main commands: `fetch` and `stats`.

### `fetch`

The `fetch` command downloads quotes from the website.

```bash
python src/cli.py fetch [OPTIONS]
```

**Options:**

*   `--pages PAGES`: The number of pages to crawl (default: 1).
*   `--tag TAG`: The tag to filter quotes by (e.g., `love`, `life`).
*   `--delay DELAY`: The delay in seconds between requests (default: 0.5).
*   `--out FILE`: The output file path (default: `data/quotes.json`).
*   `--format FORMAT`: The output format (`json` or `csv`, default: `json`).

**Examples:**

*   Fetch quotes from the first 3 pages and save them to a JSON file:

    ```bash
    python src/cli.py fetch --pages 3 --out data/quotes.json
    ```

*   Fetch quotes tagged with "life" from the first 5 pages and save them to a CSV file:

    ```bash
    python src/cli.py fetch --pages 5 --tag life --format csv --out data/life_quotes.csv
    ```

### `stats`

The `stats` command analyzes a JSON file of quotes and provides statistics.

```bash
python src/cli.py stats [OPTIONS]
```

**Options:**

*   `--src FILE`: The path to the JSON file with quotes (required).
*   `--top N`: The number of top items to display (default: 5).

**Example:**

*   Analyze the `data/quotes.json` file and show the top 10 authors and tags:

    ```bash
    python src/cli.py stats --src data/quotes.json --top 10
    ```

## Project Structure

```
.
├── data/
│   └── quotes.json
├── src/
│   ├── cli.py
│   ├── fetch.py
│   ├── models.py
│   ├── parse.py
│   └── strategies.py
├── tests/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

*   `data/`: Default directory for storing scraped data.
*   `src/`: Contains the main source code for the scraper.
    *   `cli.py`: The command-line interface.
    *   `fetch.py`: Handles fetching the HTML content.
    *   `parse.py`: Parses the HTML to extract quotes.
    *   `models.py`: Defines the data models.
    *   `strategies.py`: Implements different saving strategies.
*   `tests/`: Contains tests for the project.
*   `requirements.txt`: A list of the project's dependencies.

## Dependencies

*   [requests](https://pypi.org/project/requests/)
*   [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
*   [pathlib](https://docs.python.org/3/library/pathlib.html)
*   [collections](https://docs.python.org/3/library/collections.html)
*   [typing](https://docs.python.org/3/library/typing.html)
*   [dataclasses](https://docs.python.org/3/library/dataclasses.html)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
