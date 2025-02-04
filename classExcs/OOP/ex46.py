

class Report:
    def __init__(self, number):
        self.number = number
        self.checks = {}

    def add_check(self, name, v):
        self.checks[name] = v

    def passed(self):
        return all(self.checks.values())

    def render(self):
        s = f"Results for car #{self.number}\n"
        for name, v in self.checks.items():
            s += f"* {name}: {'OK' if v else 'Failed'}\n"
        s += "PASSED" if self.passed() else "NOT PASSED"
        return s


from car_check import Report

car1 = Report('30-210-18')

car1.add_check('Wheels', True)
car1.add_check('Brakes', True)
car1.add_check('Lights', False)
car1.add_check('Gear', True)

assert False == car1.passed()

print(car1.render())

TEST_RESULT = """Results for car #30-210-18
* Wheels: OK
* Brakes: OK
* Lights: Failed
* Gear: OK
NOT PASSED"""

assert TEST_RESULT == car1.render()

print("+++ CAR1 OK")

car2 = Report('40-444-40')

car2.add_check('Wheels', True)
car2.add_check('Brakes', True)
car2.add_check('CO', True)

assert car2.passed()

print(car2.render())

TEST_RESULT = """Results for car #40-444-40
* Wheels: OK
* Brakes: OK
* CO: OK
PASSED"""

assert TEST_RESULT == car2.render()

print("+++ CAR2 OK")