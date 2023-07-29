import requests, json, os
from flask import Flask, jsonify, request
from helpers.get_cik_number import get_cik_number
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
from config.config import Config

DATA_SEC_BASE_URL = "https://data.sec.gov"
USER_AGENT = "akulkar27@gmail.com"

app = Flask(__name__)

def get_days_difference(date_str1, date_str2):
    # Step 1: Parse the date strings into datetime objects
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')

    # Step 2: Calculate the time difference between the two dates
    time_difference = abs((date2 - date1))

    # Step 3: Return the number of days as an integer
    return time_difference.days

def get_alpha_vantage_stock_price(ticker):
    api_key = Config.ALPHA_VANTAGE_API_KEY

    ts = TimeSeries(key=api_key, output_format='json')
    data, _ = ts.get_quote_endpoint(symbol=ticker)

    stock_price = data['05. price']

    return stock_price

@app.route('/api/stock-price', methods=['POST'])
def stock_price():
    ticker = request.json['ticker']
    stock_price = get_alpha_vantage_stock_price(ticker)

    return jsonify({'ticker': ticker, 'stock_price': stock_price})

@app.route('/api/financials/company-concepts', methods=['POST'])
def get_company_concepts():
    ticker = request.json['ticker'].upper()
    fiscal_year = int(request.json['fiscal_year'])

    cik_number = get_cik_number(ticker)

    url = f"{DATA_SEC_BASE_URL}/api/xbrl/companyfacts/CIK{cik_number}.json"
    print(url)

    try:
        result = ''
        if ticker == "COST":
            costco_facts = open(os.getcwd() + '\\api\\routes\\costco_company_facts.json')
            result = json.load(costco_facts)
        else:
            headers = {'User-Agent': USER_AGENT}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()

        concepts_list = list(result['facts']['us-gaap'].keys())
        data_concepts = result['facts']['us-gaap']

        fdata = {}
        for item in concepts_list:
            data = data_concepts[item]['units']
            data_units = list(data_concepts[item]['units'].keys())
            for data_units_attr in data_units:
                for record in data[data_units_attr]:
                    if 'frame' in record:
                        if record['fy'] == fiscal_year and record['fp'] == 'FY' and record['frame'] == f"CY{fiscal_year}":
                            fdata[item] = record['val']
                    else:
                        if 'start' in record and 'end' in record:
                            if record['fy'] == fiscal_year and record['fp'] == 'FY' and get_days_difference(record['start'], record['end']) > (9*30):
                                fdata[item] = record['val']
                        elif record['fy'] ==  fiscal_year and record['fp'] == 'FY':
                            fdata[item] = record['val']

        fdata['url'] = url
        return jsonify(fdata)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500