from employee import IEmployee
from payment import PaymentProcessorFactory

class App:
    def __init__(self, available_payment_methods):
        self.available_payment_methods = available_payment_methods
        self.employees = []

    def add_employee(self, employee: IEmployee):
        self.employees.append(employee)

    
    def run(self):
        for employee in self.employees:
            employee.process_payment()
