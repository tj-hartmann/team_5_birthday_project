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


def find_birthday_groups(people):

    gruppen = {}

    for person in people:
        monat = person["birthdate"].month
        tag = person["birthdate"].day
        schluessel = (monat, tag)

        if schluessel not in gruppen:
            gruppen[schluessel] = []
        gruppen[schluessel].append(person["id"])

    result = {}

    for schluessel, value in gruppen.items():
        if len(value) > 1:
            value.sort()
            result[schluessel] = value

    return result
