# Tic Tac Toe Project
Tic Tac Toe project for the AGH PitE classes. Made by Kamil Krawiec and Adam Balski.

## Project Layout

```
Tic Tac Toe project
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
├── src
│   └── tic_tac_toe
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
└── tests
    ├── __init__.py
    └── test_example_module.py
```

## Quick Start

### 1. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
```

### 2. Install the project to make it visible to Python
```bash
pip install -e .
```
Alternatively, you can temporarily point PYTHONPATH to src.

### 2. Run the application
```bash
python -m src.tic_tac_toe.main
```

## Running Tests

Run all tests:
```bash
python -m unittest discover -s tests
```
