import requests
from flask import Blueprint, jsonify, request
from helpers.get_cik_number import get_cik_number

assets_bp = Blueprint('assets', __name__)

DATA_SEC_BASE_URL = "https://data.sec.gov"
USER_AGENT = "akulkar27@gmail.com"

@assets_bp.route('/financials/assets', methods=['POST'])
def get_assets():
    ticker = request.json['ticker']
    fiscal_year = request.json['fiscal_year']

    cik_number = get_cik_number(ticker)
    print(cik_number)

    start_date = f"{fiscal_year - 1}-12-31"
    end_date = f"{fiscal_year}-12-31"

    url = f"{DATA_SEC_BASE_URL}/api/xbrl/companyfacts/{cik_number}.json?date=start:{start_date}&date=end:{end_date}"

    try:
        headers = {'User-Agent': USER_AGENT}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        xbrl_data = response.json()

        assets = xbrl_data['facts']['us-gaap']['Assets']

        return jsonify(assets)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
