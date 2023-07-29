import requests, json
from config.config import Config
from flask import jsonify, request
from util.ticker_mappings import get_cik_number
from util.dates import get_days_difference
from os.path import join

DATA_SEC_BASE_URL = "https://data.sec.gov"
USER_AGENT = Config.USER_AGENT

def get_company_concepts(ticker, fiscal_year):
    cik_number = get_cik_number(ticker)

    url = f"{DATA_SEC_BASE_URL}/api/xbrl/companyfacts/CIK{cik_number}.json"
    print(url)

    try:
        result = ''
        if ticker == "COST":
            costco_facts = open(join('files','costco_company_facts.json'), 'r')
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