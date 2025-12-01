from resources import TaxCalculator, AccountingModule, CreditAuthService

class IFinancialDataAdapter:
    def get_data(self):
        raise NotImplementedError("Subclasses must implement this method.")


class TaxCalculatorAdapter:
    def __init__(self, tax_calculator: TaxCalculator):
        self._tax_calculator = tax_calculator

    def get_data(self):
        return self._tax_calculator.get_csv() + " as JSON"

class AccountingModuleAdapter:
    def __init__(self, accounting_module: AccountingModule):
        self._accounting_module = accounting_module

    def get_data(self):
        return self._accounting_module.get_xml() + " as JSON"
    
class CreditAuthServiceAdapter:
    def __init__(self, credit_auth_service: CreditAuthService):
        self._credit_auth_service = credit_auth_service

    def get_data(self):
        return self._credit_auth_service.get_json()