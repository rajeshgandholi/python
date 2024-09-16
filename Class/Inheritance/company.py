from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee  # noqa
"""this is a 'Has-a' relationship"""
"""A company has employees"""


class Company:
    def __init__(self) -> None:
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('--------------------')
        print('Current Employees: ')
        print('--------------------')
        for i in self.employees:
            print(i.fname, i.lname)
        print('--------------------')

    def pay_employees(self):
        print('**********************************')
        print('Paying Employees:')
        print('**********************************')
        for i in self.employees:
            print('Paycheck for: ', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')    # f string allows to include variable in a string  # noqa
            print('----------------------------------')


def main():
    my_company = Company()

    employee1 = SalaryEmployee('Rajesh', 'Gandholi', 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Sridhar', 'Gandholi', 10, 80)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Sai', 'Gandholi', 80000, 10, 25)
    my_company.add_employee(employee3)

    # print(my_company.employees)
    my_company.display_employees()
    my_company.pay_employees()


main()
