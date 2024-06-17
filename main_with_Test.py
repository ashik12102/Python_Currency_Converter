import unittest
from unittest.mock import patch
from Currency_validation import currency_validation
from Amount_validation import amount_validation
import requests

def currency_converter(from_currency,to_currency,Amount):
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={Amount}"

    payload = {}
    headers= {
            "apikey": "41ysUqRCsWqnH7xPKRbUnvpTwuxSrKC7"
                }
    response = requests.request("GET", url, headers=headers, data = payload)
    print("Converted amount will be: " + str(response.json()["result"]))

def main():
    Amount = amount_validation()
    from_currency,to_currency = currency_validation()
    currency_converter(from_currency,to_currency,Amount)


class TestCurrencyConversion(unittest.TestCase):
    @patch('builtins.input', side_effect=['USD', 'EUR'])
    def test_valid_currencies(self, mock_input):
        from_currency, to_currency = currency_validation()
        self.assertEqual(from_currency, 'USD')
        self.assertEqual(to_currency, 'EUR')

    @patch('builtins.input', side_effect=['INVALID', 'INVALID'])
    def test_invalid_currencies(self, mock_input):
        with self.assertRaises(SystemExit):
            currency_validation()

    @patch('builtins.input', side_effect=['100'])
    def test_valid_amount(self, mock_input):
        amount = amount_validation()
        self.assertEqual(amount, 100.0)

    @patch('builtins.input', side_effect=['-100'])
    def test_negative_amount(self, mock_input):
        with self.assertRaises(SystemExit):
            amount_validation()


if __name__ == "__main__":
    main()




