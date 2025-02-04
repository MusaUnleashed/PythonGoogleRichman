import json


def org_chart(dept, indent=0):
    """Returns org chart in the following format:
    [
        (indent, employee_count, title),
        ...
    ]
    """
    charts = [org_chart(d, indent + 1) for d in dept["departments"]]
    # get counts from first line in each child
    n = len(dept["members"]) + sum(c[0][1] for c in charts)
    t = (indent, n, dept["title"])
    return [t, *[x for k in charts for x in k]]  # flatten!


def render_org_chart(dept):
    lines = org_chart(dept)
    return "".join("{}- {} ({})\n".format(t[0] * "  ", t[2], t[1]) for t in lines)


with open("company3.json") as f:
    data = json.load(f)

s = render_org_chart(data)
print(s)
expected = """- ACME International (115)
  - Management (5)
  - Operations (31)
    - Human Resources (8)
    - IT (14)
      - Helpdesk (8)
    - Customer Support (6)
  - Marketing (8)
    - Sales (4)
  - Research and Development (69)
    - Software Engineering (31)
      - Web Development (6)
      - Mobile Development (3)
      - Backend Development (18)
        - Algorithms (7)
        - Computer Vision (4)
        - Graphics (5)
    - Quality Assurance (25)
      - Test Engineering (5)
      - Automation (12)
    - Data Engineering (10)
      - Cloud (6)
"""
assert s == expected

print("OK")
