import os
from pathlib import Path

class BaseConfig:
    _BASE_DIR = Path(__file__).parent
    _DB_NAME = "database.db"
    _DB_DIR = _BASE_DIR / "db"
    _DB_PATH = str(_DB_DIR / _DB_NAME)
    
    @classmethod
    def ensure_db_dir_exists(cls):
        cls._DB_DIR.mkdir(parents=True, exist_ok=True)
    
    @property
    def db_path(self):
        self.ensure_db_dir_exists()
        return self._DB_PATH

    @property
    def db_dir(self):
        self.ensure_db_dir_exists()
        return self._DB_DIR

class TestConfig:
    _BASE_DIR = Path(__file__).parent
    _DB_NAME = "test_database.db"
    _DB_DIR = _BASE_DIR / "db"
    _DB_PATH = str(_DB_DIR / _DB_NAME)
    
    @classmethod
    def ensure_db_dir_exists(cls):
        cls._DB_DIR.mkdir(parents=True, exist_ok=True)
    
    @property
    def db_path(self):
        self.ensure_db_dir_exists()
        return self._DB_PATH

    @property
    def db_dir(self):
        self.ensure_db_dir_exists()
        return self._DB_DIR
