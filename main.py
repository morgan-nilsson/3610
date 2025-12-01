from adapters import TaxCalculatorAdapter, AccountingModuleAdapter, CreditAuthServiceAdapter
from resources import TaxCalculator, AccountingModule, CreditAuthService

class ForcastingFinancialModelingModule:
    def do_something(self, data):
        return f"Processed data: {data}"

def main():

    tax_calculator = TaxCalculator()
    accounting_module = AccountingModule()
    credit_auth_service = CreditAuthService()

    tax_adapter = TaxCalculatorAdapter(tax_calculator)
    accounting_adapter = AccountingModuleAdapter(accounting_module)
    credit_adapter = CreditAuthServiceAdapter(credit_auth_service)

    forecasting_module = ForcastingFinancialModelingModule()

    tax_data = tax_adapter.get_data()
    accounting_data = accounting_adapter.get_data()
    credit_data = credit_adapter.get_data()

    print(forecasting_module.do_something(tax_data))
    print(forecasting_module.do_something(accounting_data))
    print(forecasting_module.do_something(credit_data))

if __name__ == "__main__":
    main()