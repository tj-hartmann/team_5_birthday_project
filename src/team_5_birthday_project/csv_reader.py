import csv

REQUIRED_COLUMNS = ["id", "name", "datum"]


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read the raw CSV rows without interpreting their values."""
    rows = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != REQUIRED_COLUMNS:
            raise ValueError(
                "CSV must contain exactly these columns: " + ", ".join(REQUIRED_COLUMNS)
            )

        for row in reader:
            rows.append(
                {
                    "id": (row["id"] or "").strip(),
                    "name": (row["name"] or "").strip(),
                    "datum": (row["datum"] or "").strip(),
                }
            )

    return rows
