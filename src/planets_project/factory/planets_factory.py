from typing import Any, Iterable
from src.planets_project.models.planet import Planet
from src.planets_project.cofiguration_loading.config_loader import read_config
from assets.fonts.colors_fonts import WHITE, YELLOW, BLUE, RED, DARK_GREY, PURPLE, ORANGE, GREEN, LIGHT_BLUE, PINK, LIGHT_YELLOW


# Load configuration once (your existing approach)
CONFIG = read_config()

# PRESETS are the raw dicts for each body
PRESETS: dict[str, dict[str, Any]] = {"sun": CONFIG["sun"], **CONFIG["planets"]}
DEFAULT_ORDER: list[str] = ["sun"] + list(CONFIG["planets"].keys())

# Map color names from JSON to RGB tuples used by pygame drawing
COLOR_MAP = {
    "WHITE": WHITE,
    "YELLOW": YELLOW,
    "BLUE": BLUE,
    "RED": RED,
    "DARK_GREY": DARK_GREY,
    "PURPLE": PURPLE,
    "ORANGE": ORANGE,
    "GREEN": GREEN,
    "LIGHT_BLUE": LIGHT_BLUE,
    "PINK": PINK,
    "LIGHT_YELLOW": LIGHT_YELLOW,
}

# ------- helpers -------

_REQUIRED_FIELDS = {"name", "x", "y", "radius", "color", "mass", "x_vel", "y_vel"}

def _validate_and_normalize(key: str, data: dict[str, Any]) -> dict[str, Any]:
    """Validate a single body dict from config; convert types & resolve color."""
    if not isinstance(data, dict):
        raise ValueError(f"Preset '{key}': expected object, got {type(data).__name__}")

    missing = _REQUIRED_FIELDS - data.keys()
    if missing:
        raise ValueError(f"Preset '{key}': missing required fields: {sorted(missing)}")

    # Optional: if you decide to enforce a 'type' field in files later:
    if "type" in data and data["type"] != "planet":
        raise ValueError(f"Preset '{key}': expected type 'planet', got {data['type']!r}")

    try:
        name = str(data["name"])
        x = float(data["x"])
        y = float(data["y"])
        radius = int(data["radius"])
        mass = float(data["mass"])
        x_vel = float(data["x_vel"])
        y_vel = float(data["y_vel"])
    except (TypeError, ValueError) as e:
        raise ValueError(f"Preset '{key}': invalid number/type in fields: {e}")

    color_name = str(data["color"])
    if color_name not in COLOR_MAP:
        raise ValueError(
            f"Preset '{key}': unknown color '{color_name}'. "
            f"Allowed: {', '.join(sorted(COLOR_MAP))}"
        )
    color_rgb = COLOR_MAP[color_name]

    # Optional boolean (your JSON has for the Sun)
    is_sun = bool(data.get("sun", False))

    return {
        "name": name,
        "x": x,
        "y": y,
        "radius": radius,
        "mass": mass,
        "x_vel": x_vel,
        "y_vel": y_vel,
        "color": color_rgb,
        "sun": is_sun,
    }

# ------- factory API -------

def planet_factory(preset_key: str) -> Planet:
    """
    Build a single Planet from a preset key ('sun', 'earth', ...).
    Raises ValueError on bad key or invalid data.
    """
    if preset_key not in PRESETS:
        raise ValueError(f"Unknown preset '{preset_key}'. Available: {', '.join(PRESETS)}")
    normalized = _validate_and_normalize(preset_key, PRESETS[preset_key])

    # Adapt these args to your Planet __init__ signature if it differs
    return Planet(
        name=normalized["name"],
        x=normalized["x"],
        y=normalized["y"],
        radius=normalized["radius"],
        color=normalized["color"],
        mass=normalized["mass"],
        x_vel=normalized["x_vel"],
        y_vel=normalized["y_vel"],
        is_sun=normalized["sun"],  # or 'sun=...' if your class uses that name
    )

def make_solar_system(order: Iterable[str] | None = None) -> list[Planet]:
    """
    Create a list of Planet instances in the specified order.
    Defaults to DEFAULT_ORDER (sun first, then planets).
    """
    keys = list(order) if order is not None else DEFAULT_ORDER
    planets: list[Planet] = []
    for k in keys:
        planets.append(planet_factory(k))
    return planets