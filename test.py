import requests
import os
from dotenv import load_dotenv
load_dotenv()

access_key = os.getenv("EXCHANGE_API_KEY")


def get_rate(from_currency, to_currency):
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&symbols={to_currency}"
    response = requests.get(url).json()
    return response.get("rates", {}).get(to_currency.upper())

rate = get_rate("EUR", "USD")
print("EUR to USD:", rate)