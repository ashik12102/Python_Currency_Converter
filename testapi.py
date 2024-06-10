import requests

url = "https://api.apilayer.com/fixer/symbols"
api_key = "sYOvFbbasSjMOuH7UK27PNcwpOohXlkw"

params = {
    "symbols": "DMA"
}

headers = {
    "apikey": api_key
}

response = requests.get(url, params=params, headers=headers)

status_code = response.status_code
result = response.json()

if status_code == 200:
    if "DMA" in result["symbols"]:
        print("The symbol 'DMA' is valid.")
    else:
        print("The symbol 'DMA' is not valid.")
else:
    print("Failed to retrieve data.")