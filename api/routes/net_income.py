import requests
from flask import Blueprint, jsonify, request
from helpers.get_cik_number import get_cik_number

net_income_bp = Blueprint('net_income', __name__)

DATA_SEC_BASE_URL = "https://data.sec.gov"
USER_AGENT = "akulkar27@gmail.com"

@net_income_bp.route('/financials/net_income', methods=['POST'])
def get_net_income():
    ticker = request.json['ticker'].upper()
    fiscal_year = request.json['fiscal_year']

    cik_number = get_cik_number(ticker)

    url = f"{DATA_SEC_BASE_URL}/api/xbrl/companyconcept/CIK{cik_number}/us-gaap/NetIncomeLoss.json"
    #f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik_number}/us-gaap/NetIncomeLoss.json"

    try:
        headers = {'User-Agent': USER_AGENT}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        xbrl_data = response.json()

        net_income_values = xbrl_data['units']['USD']
        net_income_dollars = None
        for net_income in net_income_values:
            if net_income['fy'] == fiscal_year:
                net_income_dollars = net_income['val']
                break

        return jsonify({"year":fiscal_year, "net_income_dollars": net_income_dollars})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
