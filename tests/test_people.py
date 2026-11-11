from datetime import date

import pytest

from team_5_birthday_project.people import load_people

"""
def test_load_people_valid(tmp_path):
    f = tmp_path / "people.csv"
    f.write_text(
        "id,name,datum\n"
        "1001,Anna Keller,2001-09-14\n"
        "1002,Ben Koch,17.03.2000\n"
        "1003,Clara Meyer,14.9.2004\n",
        encoding="utf-8",
    )

    people = load_people(str(f))

    assert len(people) == 3
    assert people[0] == {
        "id": 1001,
        "name": "Anna Keller",
        "birthdate": date(2001, 9, 14),
    }
    assert people[1]["id"] == 1002
    assert people[2]["birthdate"] == date(2004, 9, 14)
"""


def test_load_empty_csv(tmp_path):
    f = tmp_path / "empty.csv"
    f.write_text("id,name,datum\n", encoding="utf-8")

    assert load_people(str(f)) == []


"""
def test_load_people_whitespace_and_same_names(tmp_path):
    f = tmp_path / "spaces.csv"
    f.write_text(
        "id,name,datum\n"
        " 1001 , Anna Keller , 2001-09-14 \n"
        " 1002 , Anna Keller , 4.9.2001 \n",
        encoding="utf-8",
    )

    people = load_people(str(f))
    assert len(people) == 2
    assert people[0]["name"] == "Anna Keller"
    assert people[1]["name"] == "Anna Keller"
"""


def test_duplicate_id_fails(tmp_path):
    f = tmp_path / "dup.csv"
    f.write_text(
        "id,name,datum\n1001,Anna Keller,2001-09-14\n1001,Ben Koch,17.03.2000\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_people(str(f))


def test_invalid_ids_fail(tmp_path):
    for bad_id in ["0", "-5", "abc", ""]:
        f = tmp_path / f"bad_id_{bad_id}.csv"
        f.write_text(
            f"id,name,datum\n{bad_id},Anna Keller,2001-09-14\n",
            encoding="utf-8",
        )

        with pytest.raises(ValueError):
            load_people(str(f))


def test_empty_name_fails(tmp_path):
    f = tmp_path / "no_name.csv"
    f.write_text("id,name,datum\n1001,   ,2001-09-14\n", encoding="utf-8")

    with pytest.raises(ValueError):
        load_people(str(f))


def test_invalid_date_in_csv_fails(tmp_path):
    f = tmp_path / "bad_date.csv"
    f.write_text("id,name,datum\n1001,Anna Keller,29.02.2001\n", encoding="utf-8")

    with pytest.raises(ValueError):
        load_people(str(f))
