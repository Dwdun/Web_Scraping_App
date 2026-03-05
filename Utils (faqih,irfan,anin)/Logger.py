import logging
import os
import time
import requests
import functools

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("scraping_logger")
logger.setLevel(logging.DEBUG)

formatting = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

file_handler = logging.FileHandler("logs/scraper.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatting)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatting)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def retry(max_attempts=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logger.warning(f"Attempt {attempts} failed: {e}")
                    if attempts < max_attempts:
                        time.sleep(delay)
            logger.error(f"Function {func.__name__} failed after {max_attempts} attempts")
        return wrapper
    return decorator

    