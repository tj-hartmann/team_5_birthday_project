from datetime import date

import pytest

from team_5_birthday_project.dates import parse_date


def test_parse_iso_date():
    assert parse_date("2001-09-14") == date(2001, 9, 14)
    assert parse_date("2000-03-17") == date(2000, 3, 17)


def test_parse_german_date():
    assert parse_date("14.09.2001") == date(2001, 9, 14)
    assert parse_date("14.9.2001") == date(2001, 9, 14)
    assert parse_date("4.9.2001") == date(2001, 9, 4)


def test_parse_leap_year():
    assert parse_date("29.02.2004") == date(2004, 2, 29)
    assert parse_date("2000-02-29") == date(2000, 2, 29)


def test_parse_date_with_spaces():
    assert parse_date(" 2001-09-14 ") == date(2001, 9, 14)
    assert parse_date("  4.9.2001 ") == date(2001, 9, 4)


def test_invalid_calendar_dates():
    with pytest.raises(ValueError):
        parse_date("31.02.2001")

    with pytest.raises(ValueError):
        parse_date("29.02.2001")

    with pytest.raises(ValueError):
        parse_date("2001-02-29")

    with pytest.raises(ValueError):
        parse_date("32.01.2001")

    with pytest.raises(ValueError):
        parse_date("15.13.2001")


def test_invalid_date_formats():
    for bad_input in ["", "   ", "abc", "2001/09/14", "14-09-2001", "14.09.01"]:
        with pytest.raises(ValueError):
            parse_date(bad_input)
