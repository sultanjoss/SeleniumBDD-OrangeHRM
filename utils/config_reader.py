import configparser
from pathlib import Path


class ConfigReader:

    BASE_DIR = Path(__file__).resolve().parent.parent
    CONFIG_FILE = BASE_DIR / "config" / "config.ini"

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    @classmethod
    def get_base_url(cls):
        return cls.config.get(
            "environment",
            "base_url"
        )

    @classmethod
    def get_browser(cls):
        return cls.config.get(
            "browser",
            "browser"
        )

    @classmethod
    def is_headless(cls):
        return cls.config.getboolean(
            "browser",
            "headless"
        )

    @classmethod
    def get_explicit_wait(cls):
        return cls.config.getint(
            "timeouts",
            "explicit_wait"
        )