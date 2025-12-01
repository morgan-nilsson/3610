from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, employee_name, amount):
        pass


class BankTransferProcessor(IPaymentProcessor):
    def process_payment(self, employee_name, amount):
        print(f"Processing bank transfer of ${amount} to {employee_name}.")

class ChequeProcessor(IPaymentProcessor):
    def process_payment(self, employee_name, amount):
        print(f"Issuing cheque of ${amount} to {employee_name}.")

class DigitalWalletProcessor(IPaymentProcessor):
    def process_payment(self, employee_name, amount):
        print(f"Transferring ${amount} to {employee_name}'s digital wallet.")

class PaymentProcessorFactory:
    @staticmethod
    def get_payment_processor(method):
        if method == "bank_transfer":
            return BankTransferProcessor()
        elif method == "cheque":
            return ChequeProcessor()
        elif method == "digital_wallet":
            return DigitalWalletProcessor()
        else:
            raise ValueError(f"Unknown payment method: {method}")