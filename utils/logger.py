import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str, level=logging.INFO):
    """
    Creates a robust, reusable logger with:
    - Console logging
    - Rotating file logging
    - Safe handler initialization (no duplicates)
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:  # Prevent duplicate handlers
        return logger

    # ----------- FORMATTERS -----------
    log_format = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")

    # ----------- CONSOLE HANDLER -----------
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # ----------- FILE HANDLER -----------
    file_path = os.path.join(LOG_DIR, f"{name}.log")
    file_handler = RotatingFileHandler(
        file_path,
        maxBytes=500_000,  
        backupCount=3      
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False

    logger.info("Logger initialized successfully.")
    return logger

