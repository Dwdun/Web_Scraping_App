import dateparser

def parse_date(date_str):
    # parse berbagai format tanggal (indo/inggris)
    if not date_str:
        return None

    result = dateparser.parse(date_str, languages=["id", "en"])
    return result.date() if result else None