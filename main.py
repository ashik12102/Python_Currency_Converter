import requests
import Currency_validation
import Amount_validation


url = f"https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers= {
  "apikey": "sYOvFbbasSjMOuH7UK27PNcwpOohXlkw"
  }
response = requests.request("GET", url, headers=headers, data = payload)
print(response.json())
# Run this file for test