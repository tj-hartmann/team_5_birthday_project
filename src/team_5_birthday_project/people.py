from src.team_5_birthday_project.csv_reader import read_csv_rows
from src.team_5_birthday_projectbirthday_project.dates import parse_date

def load_people(path: str) -> list[dict]:
    people = []

    for row in read_csv_rows(path):
        people.append(
            {
                "id": int(row["id"]),
                "name": row["name"],
                "birthdate": parse_date(row["datum"]),
            }
        )

    return people