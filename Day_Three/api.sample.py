import requests
"""Getting of currencies before the application starts"""
currency_data = requests.get('https://openexchangerates.org/api/latest.json?app_id=a3db7dbfca7744ca93488b91fdd84eba')
"""Asking the user for the currency code"""
currency_code = input("Please enter the Currency Code: ")
"""Asking the user for amount in dollars"""
amount = input("Please enter the amount in USD to be converted: ")
def getCurrency(currency_code, amount):
    """Reading through the json data to get the currency code"""
    currency = currency_data.json()['rates'][currency_code]
    """Multiplying the local currency with amount"""
    converted_amount = currency * float(amount)
    """Printing the result"""
    print(" > " + amount + " dollars  is " + currency_code + " " + str(converted_amount))
getCurrency(currency_code, amount)