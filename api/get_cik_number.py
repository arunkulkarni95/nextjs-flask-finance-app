import requests
from flask import request
from functools import lru_cache

@lru_cache(maxsize=1)
def load_ticker_mappings():
    try:
        url = "https://www.sec.gov/files/company_tickers.json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception("Failed to load ticker mappings: " + str(e))

def get_cik_number(ticker):
    ticker = ticker.upper()
    if ticker == 'TWTR':
        cik_number = '0001418091'
        return cik_number
    else: 
        mappings = load_ticker_mappings()
        cik_number = None
        for _, value in mappings.items():
            if (value["ticker"] == ticker):
                cik_number = str(value['cik_str']).zfill(10)
                return cik_number
                