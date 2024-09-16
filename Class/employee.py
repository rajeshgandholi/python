"""Demo: company payroll with classes"""


class Employee:
    def __init__(self, fname, lname, salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52       # believing the salary is split equally among the 52 weeks in a year   # noqa
