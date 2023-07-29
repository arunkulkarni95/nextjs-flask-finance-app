import requests
from flask import Blueprint, jsonify, request
from functools import lru_cache

shares_outstanding_bp = Blueprint('shares_outstanding', __name__)

DATA_SEC_BASE_URL = "https://data.sec.gov"
USER_AGENT = "akulkar27@gmail.com"

@lru_cache(maxsize=1)
def load_ticker_mappings():
    try:
        url = "https://www.sec.gov/files/company_tickers.json"
        response = requests.get(url)
        response.raise_for_status()
        mappings = response.json()
        return mappings
    except requests.exceptions.RequestException as e:
        raise Exception("Failed to load ticker mappings: " + str(e))

@shares_outstanding_bp.route('/financials/shares_outstanding', methods=['POST'])
def get_shares_outstanding():
    ticker = request.json['ticker']
    fiscal_year = request.json['fiscal_year']

    mappings = load_ticker_mappings()
    cik_number = mappings.get(ticker, "").zfill(10)

    start_date = f"{fiscal_year - 1}-12-31"
    end_date = f"{fiscal_year}-12-31"

    url = f"{DATA_SEC_BASE_URL}/api/xbrl/companyfacts/{cik_number}.json?date=start:{start_date}&date=end:{end_date}"

    try:
        headers = {'User-Agent': USER_AGENT}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        xbrl_data = response.json()

        shares_outstanding = xbrl_data['facts']['dei']['EntityCommonStockSharesOutstanding']['units']['shares']

        return jsonify(shares_outstanding)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
