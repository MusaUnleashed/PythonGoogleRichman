import json


def number_of_employees(company):
    return sum(len(dept["members"]) for dept in company)


def total_salaries(company):
    return sum(p["salary"] for dept in company for p in dept["members"])


with open("company2.json") as f:
    data = json.load(f)

num = number_of_employees(data)
print("Total employees:", num)
assert num == 66
print("OK1")

salary = total_salaries(data)
print("Total salary:", salary)
assert salary == 1338800
print("OK2")

print("Done!")
