## Project Layout

```
PythonInTheEnterprise2025_Monday/
├── src/planets_project/
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py
│   ├── config.py
│   ├── main.py
│   ├── event_handling/
│   │   ├── __init__.py
│   │   ├── event_bus.py
│   │   └── events.py
│   ├── factory/
│   │   ├── __init__.py
│   │   ├── planets_factory.py
│   │   └── stars_factory.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── body.py
│   │   ├── planet.py
│   │   └── star.py
│   ├── physics_engine/
│   │   ├── __init__.py
│   │   ├── forces.py
│   │   └── integrators.py
│   ├── renderer/
│   │   ├── __init__.py
│   │   └── renderer.py
│   ├── sandbox_feature/
│   │   ├── __init__.py
│   │   └── sandbox.py
├── tests/
│   ├── __init__.py
├── assets/
│   ├── buttons/
│   ├── fonts/
│   │   └── colors_fonts.py
│   ├── planets/
│   ├── LICENSE
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   └── setup.cfg
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
python -m src.planets_project.main```