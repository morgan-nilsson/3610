from abc import ABC, abstractmethod

class IEmployee(ABC):
    def __init__(self, name, payment_processor):
        self.name = name
        self.payment_processor = payment_processor

    @abstractmethod
    def calculate_salary(self):
        pass

    def process_payment(self):
        amount = self.calculate_salary()
        self.payment_processor.process_payment(self.name, amount)


class HourlyEmployee(IEmployee):
    def __init__(self, name, hourly_rate, hours_worked, payment_processor):
        super().__init__(name, payment_processor)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
class SalariedEmployee(IEmployee):
    def __init__(self, name, monthly_salary, payment_processor):
        super().__init__(name, payment_processor)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
    
class Contractor(IEmployee):
    def __init__(self, name, project_fee, payment_processor):
        super().__init__(name, payment_processor)
        self.project_fee = project_fee

    def calculate_salary(self):
        return self.project_fee