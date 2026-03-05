import dateparser
from datetime import datetime

def parse_date(date_str):
    # parse berbagai format tanggal (indo/inggris)
    # bisa baca bahasa Indonesia & Inggris
    if not date_str:
        return None

    try:
        result = dateparser.parse(date_str, languages=["id", "en"])
        return result.date() if result else None
    except Exception:
        return None