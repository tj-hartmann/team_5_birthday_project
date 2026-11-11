import datetime


def parse_date(text: str) -> datetime.date:
    return datetime.datetime.strptime(text, "%d.%m.%Y").date()
