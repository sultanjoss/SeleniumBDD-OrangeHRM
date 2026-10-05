import logging
from pathlib import Path


class LoggerUtils:

    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_DIR = BASE_DIR / "logs"
    LOG_FILE = LOG_DIR / "test.log"

    @classmethod
    def get_logger(cls, name):
        cls.LOG_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                cls.LOG_FILE,
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger