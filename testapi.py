import requests

url = "https://api.apilayer.com/fixer/symbols"
api_key = "sYOvFbbasSjMOuH7UK27PNcwpOohXlkw"

symbol = input("Enter the currency symbol: ")

params = {
    "symbols": symbol
}

headers = {
    "apikey": api_key
}

response = requests.get(url, params=params, headers=headers)

status_code = response.status_code
result = response.json()

if status_code == 200:
    if symbol in result["symbols"]:
        print(f"The symbol '{symbol}' is valid.")
    else:
        print(f"The symbol '{symbol}' is not valid.")
else:
    print("Failed to retrieve data.")