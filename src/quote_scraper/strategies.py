import json
import csv
from pathlib import Path
from abc import ABC, abstractmethod
from typing import List

from models import Quote


class SaveStrategy(ABC):
    """Abstract base class for save strategies."""

    @abstractmethod
    def save(self, quotes: List[Quote], output_path: Path) -> None:
        """
        Save the given quotes to the specified output path.

        :param quotes: list of Quote objects
        :param output_path: destination Path
        """
        raise NotImplementedError


class JsonSaveStrategy(SaveStrategy):
    """Save quotes as a JSON file (UTF-8)."""

    def save(self, quotes: List[Quote], output_path: Path) -> None:
        data = [q.__dict__ for q in quotes]
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[DONE] Saved {len(quotes)} quotes to {output_path} (JSON).")


class CsvSaveStrategy(SaveStrategy):
    """Save quotes as a CSV file (UTF-8)."""

    def save(self, quotes: List[Quote], output_path: Path) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["text", "author", "tags"])
            for q in quotes:
                writer.writerow([q.text, q.author, "|".join(q.tags)])
        print(f"[DONE] Saved {len(quotes)} quotes to {output_path} (CSV).")


class StrategyFactory:
    """
    Small factory to obtain a SaveStrategy by name.
    Extend the _strategies map to add new formats.
    """
    _strategies = {
        "json": JsonSaveStrategy,
        "csv": CsvSaveStrategy,
    }

    @classmethod
    def get(cls, name: str) -> SaveStrategy:
        try:
            strategy_cls = cls._strategies[name]
            return strategy_cls()
        except KeyError:
            raise ValueError(f"Unsupported format: {name!r}. Available: {', '.join(cls._strategies.keys())}")