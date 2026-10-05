import platform
import sys
from pathlib import Path

from utils.config_reader import ConfigReader


class AllureUtils:

    BASE_DIR = Path(__file__).resolve().parent.parent
    ALLURE_RESULTS_DIR = BASE_DIR / "allure-results"

    @classmethod
    def create_environment_file(cls):

        cls.ALLURE_RESULTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        environment_file = (
            cls.ALLURE_RESULTS_DIR / "environment.properties"
        )

        environment_data = {
            "Application": "OrangeHRM",
            "Base.URL": ConfigReader.get_base_url(),
            "Browser": ConfigReader.get_browser(),
            "Headless": str(
                ConfigReader.is_headless()
            ).lower(),
            "Operating.System": platform.system(),
            "Python.Version": platform.python_version()
        }

        with open(
            environment_file,
            "w",
            encoding="utf-8"
        ) as file:

            for key, value in environment_data.items():
                file.write(f"{key}={value}\n")