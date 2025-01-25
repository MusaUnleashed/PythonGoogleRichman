# company_flat1.py
import json
from pprint import pprint


def total_salaries(people):
    total = 0
    for emp in people:
        total += emp["salary"]
    return total
    # ---- YOUR CODE HERE -----------------
    pass
    # -------------------------------------


def total_salaries_for_position(people, position):
    # ---- YOUR CODE HERE -----------------
    salary_by_position = {}
    total = 0
    for emp in people:
        if emp["position"] == position:
            total += emp["salary"]
    return total
    pass
    # -------------------------------------


with open("company1.json") as f:
    all_employees = json.load(f)

result1 = total_salaries(all_employees)
print("Total salary:", result1)
assert result1 == 1979800
print("OK1")

# result2 = total_salaries_for_position(all_employees, "Developer")
# print("Developers' salary:", result2)
# assert result2 == 1073700
# print("OK2")
# #
# result3 = total_salaries_for_position(all_employees, "Team Leader")
# print("Team Leaders' salary:", result3)
# assert result3 == 376100
# print("OK3")
#
# print("Done!")
