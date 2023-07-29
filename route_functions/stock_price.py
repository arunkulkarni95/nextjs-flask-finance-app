from flask import jsonify, request
from util.alpha_vantage import get_alpha_vantage_stock_price

def get_stock_price(ticker):
    ticker = request.json['ticker']
    stock_price = get_alpha_vantage_stock_price(ticker)

    return jsonify({'ticker': ticker, 'stock_price': stock_price})