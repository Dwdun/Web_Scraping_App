import logging
import os

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

