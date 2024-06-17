import requests

def currency_validation():
    while True:
        from_currency = input(" Enter currency to be converted from:  ").upper().strip()
        to_currency = input(" Enter currency to be converted to:  ").upper().strip()

        url = "https://api.apilayer.com/fixer/symbols"
        api_key = "KzCaw3bjb1V92e1n8V421ucVnZ0XTAEI"

        params = {
            "symbols": f"{from_currency},{to_currency}"
        }

        headers = {
            "apikey": api_key
        }

        response = requests.get(url, params=params, headers=headers)

        status_code = response.status_code
        result = response.json()

        if status_code == 200:
          
            if from_currency in result["symbols"] and to_currency in result["symbols"]:
                    return from_currency,to_currency
            else:
                    if from_currency not in result["symbols"]:                         
                        print(f"The currency '{from_currency}' is not valid.")
                    if to_currency not in result["symbols"]:                         
                        print(f"The currency '{to_currency}' is not valid.")    
        else:
            print("Failed to retrieve data. Please try again")
