from abc import ABC
from abc import abstractmethod

class Customer:
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    primary_email: str | None
    secondary_email: str | None
    primary_phone_number: str | None
    secondary_phone_number: str | None

    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.middle_name = None
        self.primary_email = None
        self.secondary_email = None
        self.primary_phone_number = None
        self.secondary_phone_number = None

    def __repr__(self) -> str:
        return f"Customer(first_name={self.first_name}, last_name={self.last_name}, middle_name={self.middle_name}, primary_email={self.primary_email}, secondary_email={self.secondary_email}, primary_phone_number={self.primary_phone_number}, secondary_phone_number={self.secondary_phone_number})"

class ICustomerBuilder(ABC):
    customer: Customer

    def __init__(self) -> None:
        self.customer = Customer()

    def firstName(self, name: str):
        self.customer.first_name = name
        return self

    def lastName(self, name: str):
        self.customer.last_name = name
        return self

    def middleName(self, name: str):
        self.customer.middle_name = name
        return self

    def primaryEmail(self, email: str):
        self.customer.primary_email = email
        return self
    
    def secondaryEmail(self, email: str):
        self.customer.secondary_email = email
        return self
    
    def primaryPhoneNumber(self, phone_number: str):
        self.customer.primary_phone_number = phone_number
        return self
    
    def secondaryPhoneNumber(self, phone_number: str):
        self.customer.secondary_phone_number = phone_number
        return self

    @abstractmethod
    def build(self) -> Customer:
        pass

class WebAppBuilder(ICustomerBuilder):
    def __init__(self) -> None:
        super().__init__()

    def build(self) -> Customer:
        if not self.customer.first_name:
            raise ValueError("First name is required")
        if not self.customer.last_name:
            raise ValueError("Last name is required")
        if not self.customer.middle_name:
            raise ValueError("Middle name is required")
        if not self.customer.primary_email:
            raise ValueError("Primary email is required")
        if not self.customer.secondary_email:
            raise ValueError("Secondary email is required")
        if not self.customer.primary_phone_number:
            raise ValueError("Primary phone number is required")
        if not self.customer.secondary_phone_number:
            raise ValueError("Secondary phone number is required")
        return self.customer

# doesn't need middleName, secondaryEmail and secondaryMobileNumber
class MobileAppBuilder(ICustomerBuilder):
    def __init__(self) -> None:
        super().__init__()

    def build(self) -> Customer:
        if not self.customer.first_name:
            raise ValueError("First name is required")
        if not self.customer.last_name:
            raise ValueError("Last name is required")
        if not self.customer.primary_email:
            raise ValueError("Primary email is required")
        if not self.customer.primary_phone_number:
            raise ValueError("Primary phone number is required")
        return self.customer
