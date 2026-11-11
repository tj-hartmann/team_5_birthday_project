import pytest
from birthday_project.csv_reader import read_csv_rows


def test_read_csv_normal(tmp_path):
    p = tmp_path / "test.csv"
    p.write_text(
        "id,name,datum\n1001,Anna Keller,2001-09-14\n1002,Ben Koch,17.03.2000\n",
        encoding="utf-8",
    )

    res = read_csv_rows(str(p))

    assert len(res) == 2
    assert res[0] == {"id": "1001", "name": "Anna Keller", "datum": "2001-09-14"}
    assert res[1]["name"] == "Ben Koch"


def test_read_csv_spaces(tmp_path):
    p = tmp_path / "spaces.csv"
    p.write_text("id,name,datum\n 1001 , Anna Keller , 2001-09-14 \n", encoding="utf-8")

    res = read_csv_rows(str(p))
    assert res[0] == {"id": "1001", "name": "Anna Keller", "datum": "2001-09-14"}


def test_read_csv_empty(tmp_path):
    p = tmp_path / "empty.csv"
    p.write_text("id,name,datum\n", encoding="utf-8")

    assert read_csv_rows(str(p)) == []


def test_read_csv_wrong_header(tmp_path):
    p = tmp_path / "wrong.csv"
    p.write_text("id,name,geburtsdatum\n1001,Anna,2001-09-14\n", encoding="utf-8")

    with pytest.raises(ValueError):
        read_csv_rows(str(p))


def test_read_csv_missing_column(tmp_path):
    p = tmp_path / "missing.csv"
    p.write_text("id,name\n1001,Anna\n", encoding="utf-8")

    with pytest.raises(ValueError):
        read_csv_rows(str(p))
