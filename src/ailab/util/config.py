from pathlib import Path
import yaml

class Config:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self):
        try:
            with open(self.config_path, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise RuntimeError(f"Config file not found: {self.config_path}")
        except yaml.YAMLError as e:
            raise RuntimeError(f"Invalid YAML: {e}")   