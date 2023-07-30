from flask import Flask, request
from route_functions.stock_price import get_stock_price 
from route_functions.company_concepts import get_company_concepts

app = Flask(__name__)

@app.route('/api/stock-price', methods=['POST'])
def stock_price():
    ticker = request.json['ticker']
    return get_stock_price(ticker)

@app.route('/api/company-concepts', methods=['POST'])
def company_concepts():
    try:
        ticker = request.json['ticker'].upper()
        fiscal_year = int(request.json['fiscal_year'])
        num_hist_years = int(request.json['num_years'])
    except (KeyError, ValueError):
        # Handle malformed JSON parameters
        num_hist_years = 1

    if num_hist_years > 10:
        # Cap num_hist_years to a maximum of 10
        num_hist_years = 10

    return get_company_concepts(ticker, fiscal_year, num_hist_years)
