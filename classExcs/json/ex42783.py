import json
from pprint import pp


def salary_info(people):
    data = [p["salary"] for p in people]
    return {
        "top": max(data),
        "low": min(data),
        "avg": sum(data) // len(data),
    }


def salary_info_across_departments(company):
    return {d["title"]: salary_info(d["members"]) for d in company}


with open("company2.json") as f:
    data = json.load(f)

d = salary_info(data[0]["members"])
print("Salary info 1:", d)
assert d == {
    "top": 27200,
    "low": 12300,
    "avg": 20583,
}
print("OK1")

d = salary_info(data[-1]["members"])
print("Salary info 2:", d)
assert d == {
    "top": 27500,
    "low": 12000,
    "avg": 16916,
}
print("OK2")

all_info = salary_info_across_departments(data)
print("Company info:")
pp(all_info)
assert all_info == {
    "Hardware Engineering": {"top": 27200, "low": 12300, "avg": 20583},
    "Software Engineering": {"top": 28000, "low": 15300, "avg": 21841},
    "Sales": {"top": 26800, "low": 12600, "avg": 17087},
    "Quality Assurance": {"top": 27100, "low": 13100, "avg": 21272},
    "Human Resources": {"top": 27500, "low": 12000, "avg": 16916},
}
print("OK3")

print("Done!")
