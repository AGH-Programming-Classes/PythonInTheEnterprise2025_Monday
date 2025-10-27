from typing import Dict, Any, Iterable, Optional
from src.planets_project.models.planet import Planet
from assets.planets.default_planets import PRESETS, DEFAULT_ORDER

def planet_factory(kind: str, **overrides) -> Planet:
    """Create a single Planet from a named preset, with optional overrides."""
    key = kind.lower()
    if key not in PRESETS:
        raise ValueError(f"Unknown body type '{kind}'. Known: {', '.join(sorted(PRESETS))}")

    cfg: Dict[str, Any] = {**PRESETS[key], **overrides}

    p = Planet(cfg["x"], cfg["y"], cfg["radius"], cfg["color"], cfg["mass"], name=cfg["name"])
    p.x_vel = cfg.get("x_vel", 0.0)
    p.y_vel = cfg.get("y_vel", 0.0)
    if cfg.get("sun"):
        p.sun = True
    return p

def make_solar_system(
    order: Optional[Iterable[str]] = None,
    per_body_overrides: Optional[Dict[str, Dict[str, Any]]] = None,
):
    """
    Build a list of Planet instances in the given order.
    - order: iterable of names (defaults to DEFAULT_ORDER)
    - per_body_overrides: dict like {"earth": {"x": -0.95*Planet.AU}, ...}
    """
    if order is None:
        order = DEFAULT_ORDER
    planets = []
    for name in order:
        overrides = (per_body_overrides or {}).get(name, {})
        planets.append(planet_factory(name, **overrides))
    return planets
