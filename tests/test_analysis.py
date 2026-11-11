from datetime import date

from team_5_birthday_project.analysis import find_age_neighbors, find_birthday_groups


def test_neighbors_empty():
    assert find_age_neighbors([]) == {}


def test_neighbors_n_zero():
    people = [
        {"id": 1, "name": "Anna", "birthdate": date(2001, 9, 14)},
        {"id": 2, "name": "Ben", "birthdate": date(2001, 9, 15)},
    ]
    assert find_age_neighbors(people, n=0) == {1: [], 2: []}


def test_neighbors_distance_and_tie_breaker():
    people = [
        {"id": 10, "name": "Anna", "birthdate": date(2001, 9, 14)},
        {"id": 30, "name": "Ben", "birthdate": date(2001, 9, 13)},
        {"id": 20, "name": "Clara", "birthdate": date(2001, 9, 15)},
        {"id": 40, "name": "David", "birthdate": date(2002, 5, 1)},
    ]

    res = find_age_neighbors(people, n=2)

    assert 10 not in res[10]
    assert res[10] == [20, 30]


def test_neighbors_fewer_people_than_n():
    people = [
        {"id": 1, "name": "Anna", "birthdate": date(2000, 1, 10)},
        {"id": 2, "name": "Ben", "birthdate": date(2000, 1, 20)},
        {"id": 3, "name": "Clara", "birthdate": date(2000, 1, 12)},
    ]

    res = find_age_neighbors(people, n=10)
    assert res[1] == [3, 2]


def test_neighbors_default_limit_10():
    people = []
    for i in range(1, 15):
        people.append({"id": i, "name": f"P{i}", "birthdate": date(2000, 1, i)})

    res = find_age_neighbors(people)
    assert len(res[1]) == 10
    assert 1 not in res[1]


def test_neighbors_order_independent_and_input_unchanged():
    p1 = {"id": 3, "name": "Clara", "birthdate": date(2000, 5, 10)}
    p2 = {"id": 1, "name": "Anna", "birthdate": date(2000, 5, 9)}
    p3 = {"id": 2, "name": "Ben", "birthdate": date(2000, 5, 11)}

    people = [p1, p2, p3]
    people_reversed = [p3, p2, p1]

    res1 = find_age_neighbors(people)
    res2 = find_age_neighbors(people_reversed)

    assert res1 == res2
    assert [p["id"] for p in people] == [3, 1, 2]


def test_birthday_groups_empty():
    assert find_birthday_groups([]) == {}


def test_birthday_groups_normal_and_sorted():
    people = [
        {"id": 1005, "name": "Anna", "birthdate": date(2001, 9, 14)},
        {"id": 1001, "name": "Ben", "birthdate": date(1998, 9, 14)},
        {"id": 1003, "name": "Clara", "birthdate": date(2004, 9, 14)},
        {"id": 1009, "name": "Single", "birthdate": date(2000, 3, 17)},
    ]

    groups = find_birthday_groups(people)

    assert groups == {(9, 14): [1001, 1003, 1005]}
    assert (3, 17) not in groups
    assert [p["id"] for p in people] == [1005, 1001, 1003, 1009]