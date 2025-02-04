import json


def number_of_employees(dept):
    n = len(dept["members"])
    return n + sum(number_of_employees(d) for d in dept["departments"])


def total_salaries(dept):
    v = sum(p["salary"] for p in dept["members"])
    return v + sum(total_salaries(d) for d in dept["departments"])


with open("company3.json") as f:
    data = json.load(f)

num = number_of_employees(data)
print("Total employees:", num)
assert num == 115
print("OK1")

salary = total_salaries(data)
print("Total salary:", salary)
assert salary == 2341200
print("OK2")

print("Done!")
