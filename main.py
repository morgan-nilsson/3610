# Let’s imagine that we need to develop an App for the HR system designed for automation of salary processing.
# 
# However, in the HR system we have different ways of calculating salaries:
# 
#     Hourly employees: Paid based on hours worked.
# 
#     Salaried employees: Paid a fixed monthly amount.
# 
#     Contractors: Paid based on project deliverables.
# 
# At the same time, there could be different payment methods:
# 
#     bank transfer,
# 
#     cheque,
# 
#     digital wallet.
# 
# Without a flexible approach, you would end up writing repetitive code for each combination of employee type and payment method. This would make your system hard to maintain and scale.
# 
# Tasks:
# 
#     Implement concrete classes for specific implementations (for 3 Payment Methods)
# 
#     Use a Factory Method to build different concrete implementators (available Payment Methods stored as an attribute within a Factory Method class).
# 
#     Create refined abstraction classes that extend the employee's abstraction. Such class will delegate ProcessPayment() operation to the appropriate implementation based on runtime configurations
# 
#     Create required Payment Methods via a Factory Method (might be stored within an App class as a AvalPaymentMethods property)
# 
#     Create refined abstractions and link them with concrete implementations (salaried employee -> bank transfer, hourly employee -> cheque, contractor ->digital wallet)
# 
#     Launch the App to make payments

from employee import SalariedEmployee, HourlyEmployee, Contractor
from payment import PaymentProcessorFactory
from app import App

def main():
    available_payment_methods = ["bank_transfer", "cheque", "digital_wallet"]
    app = App(available_payment_methods)

    bank_transfer_processor = PaymentProcessorFactory.get_payment_processor("bank_transfer")
    cheque_processor = PaymentProcessorFactory.get_payment_processor("cheque")
    digital_wallet_processor = PaymentProcessorFactory.get_payment_processor("digital_wallet")

    # Create employees with different payment methods
    hourly_employee = HourlyEmployee("Alice", hourly_rate=20, hours_worked=80, payment_processor=cheque_processor)
    salaried_employee = SalariedEmployee("Bob", monthly_salary=3000, payment_processor=bank_transfer_processor)
    contractor = Contractor("Charlie", project_fee=5000, payment_processor=digital_wallet_processor)

    app.add_employee(hourly_employee)
    app.add_employee(salaried_employee)
    app.add_employee(contractor)

    app.run()

if __name__ == "__main__":
    main()