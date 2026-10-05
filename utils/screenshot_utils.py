from datetime import datetime
from pathlib import Path


class ScreenshotUtils:

    BASE_DIR = Path(__file__).resolve().parent.parent
    SCREENSHOT_DIR = BASE_DIR / "screenshots"

    @classmethod
    def take_screenshot(cls, driver, scenario_name):

        cls.SCREENSHOT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        safe_name = scenario_name.replace(" ", "_")

        file_name = f"{safe_name}_{timestamp}.png"

        file_path = cls.SCREENSHOT_DIR / file_name

        driver.save_screenshot(
            str(file_path)
        )

        return file_path