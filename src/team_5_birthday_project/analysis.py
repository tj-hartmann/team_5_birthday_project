def find_age_neighbors(people, n=10):
    if n < 0:
        raise ValueError("n darf nicht negativ sein")

    result = {}

    for person in people:
        abstaende = []

        for other in people:
            if other["id"] == person["id"]:
                continue
            tage = abs((person["birthdate"] - other["birthdate"]).days)
            abstaende.append((tage, other["id"]))

        abstaende.sort()

        ids = []
        for tage, other_id in abstaende[:n]:
            ids.append(other_id)

        result[person["id"]] = ids

    return result