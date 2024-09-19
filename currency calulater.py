# Dictionary to store exchange rates
exchange_rates = {
    'USD': 1.0,       # Base currency
    'EUR': 0.85,     # 1 USD = 0.85 EUR
    'GBP': 0.75,     # 1 USD = 0.75 GBP
    'INR': 74.0,     # 1 USD = 74 INR
}

def convert_currency(amount, from_currency, to_currency):
    """Convert amount from one currency to another."""
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Unsupported currency.")
    
    # Convert amount to USD first, then to the target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

# User input
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency you want to convert from (USD, EUR, GBP, INR): ").upper()
to_currency = input("Enter the currency you want to convert to (USD, EUR, GBP, INR): ").upper()

try:
    # Perform conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
except ValueError as e:
    print(e)
    