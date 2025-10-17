# Magball Project

A simple Python project that allows you to simulate and interact with magnetic balls. The project includes basic functionalities to create, manipulate, and visualize magnetic balls in a 2D space.

## Authors

- Szymon Cichowski
- Artur Zamorowski

## Project Layout

```txt
magball/
├── src/magball_project/
│   ├── main.py
│   └── __init__.py
├── tests/
│   └── test_magball.py
├── pyproject.toml
├── requirements.txt
├── setup.cfg
└── README.md
```

## Quick Start

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
```

### 2. Install the project to make it visible to Python

```bash
pip install -e .
```

Alternatively, you can temporarily point PYTHONPATH to src.

### 2. Run the application

```bash
python -m magball_project.main
```

## Running Tests

Run all tests:

```bash
python -m unittest discover -s tests
```
