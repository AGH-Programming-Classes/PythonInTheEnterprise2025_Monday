import json
import os

def read_config(directory: str = "assets/config_files", filename: str = "default.json") -> dict:
    filepath = os.path.join(os.path.dirname(__file__), "../../../", directory, filename)
    
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Configuration file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        config = json.load(file)
    
    return config

def write_config(config: dict, directory: str, filename: str = "config.json") -> None:
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4)