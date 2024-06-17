from Currency_validation import currency_validation
from Amount_validation import amount_validation
import requests

def currency_converter(from_currency,to_currency,Amount):
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={Amount}"

    payload = {}
    headers= {
            "apikey": "sYOvFbbasSjMOuH7UK27PNcwpOohXlkw"
                }
    response = requests.request("GET", url, headers=headers, data = payload)
    print("Converted amount will be: " + str(response.json()["result"]))

def main():
    Amount = amount_validation()
    from_currency,to_currency = currency_validation()
    currency_converter(from_currency,to_currency,Amount)

if __name__ == "__main__":
    main()




