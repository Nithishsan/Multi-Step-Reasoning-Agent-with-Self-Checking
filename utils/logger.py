import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name: str, level=logging.INFO) -> logging.Logger:
    """
    Creates and returns a configured logger with:
    - Console output
    - Rotating file logging
    - Safe handler initialization
    - Timestamped, readable format
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers in Streamlit reruns
    if logger.handlers:
        return logger

    # ---------- FORMAT ----------
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ---------- CONSOLE HANDLER ----------
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # ---------- FILE HANDLER ----------
    file_path = os.path.join(LOG_DIR, f"{name}.log")
    file_handler = RotatingFileHandler(
        file_path,
        maxBytes=1_000_000,   # 1 MB
        backupCount=5
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False

    logger.info("Logger initialized")

    return logger
