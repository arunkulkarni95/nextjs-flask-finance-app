from flask import Flask, request
from route_functions.stock_price import get_stock_price 
from route_functions.company_concepts import get_company_concepts

app = Flask(__name__)

@app.route('/api/stock-price', methods=['POST'])
def stock_price():
    ticker = request.json['ticker']
    return get_stock_price(ticker)

@app.route('/api/financials/company-concepts', methods=['POST'])
def company_concepts():
    ticker = request.json['ticker'].upper()
    fiscal_year = int(request.json['fiscal_year'])
    return get_company_concepts(ticker, fiscal_year)