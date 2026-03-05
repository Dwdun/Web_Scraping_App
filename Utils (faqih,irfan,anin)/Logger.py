import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

formatting = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )