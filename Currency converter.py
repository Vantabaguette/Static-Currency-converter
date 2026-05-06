# Currency converter

exchange_rates = {
    "USD" : 1.0,
    "EUR" : 0.85,
    "GBP" : 0.75,
    "JPY" : 110.0,
    "AUD" : 1.35,
    "CAD" : 1.25,
    "INR" : 84.0,
}

def converter(amount, from_currency, to_currency):
    """Calculates and prints the converted amount."""
    
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("A currency code is invalid, something went wrong my guy!")
    
    
    amount_in_usd = amount / exchange_rates[from_currency]
    
    
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
   
    print(f"\n{amount:,.2f} {from_currency} is equal to:")
    print(f"**{converted_amount:,.2f} {to_currency}**")




def get_valid_amount():
    """Prompts dude until a valid, positive float amount is entered."""
    while True:
        try:
            amount = float(input("Enter the amount you wanna convert my dude: "))
            if amount > 0:
                return amount
            else:
                print("Amount must be a positive number, my guy.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_currency(prompt_message, rates):
    """Prompts bro until a supported currency code is entered."""
    while True:
        currency = input(prompt_message).upper()
        if currency in rates:
            return currency
        else:
            print(f"Invalid currency code. Please choose from: {', '.join(rates.keys())}")




print("\n--- Welcome to the Currency Converter, My Dude! ---")
available_currencies = ", ".join(exchange_rates.keys())
print(f"Supported Currencies: **{available_currencies}**")


while True:
    try:
        
        amount = get_valid_amount()
        from_currency = get_valid_currency("Enter the currency to convert from (e.g., USD): ", exchange_rates)
        to_currency = get_valid_currency("Enter the currency to convert it to (e.g., JPY): ", exchange_rates)

       
        converter(amount, from_currency, to_currency)
        
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")

    
    another_conversion = input("\nDo you want to perform another conversion? (yes/no): ").lower()
    if another_conversion in ('no', 'n'):
        print("Thanks for converting, see ya!")
        break 