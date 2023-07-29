# from flask import Flask, jsonify, request
# from alpha_vantage.timeseries import TimeSeries
# from config.config import Config

# app = Flask(__name__)

# def get_alpha_vantage_stock_price(ticker):
#     api_key = Config.ALPHA_VANTAGE_API_KEY

#     ts = TimeSeries(key=api_key, output_format='json')
#     data, _ = ts.get_quote_endpoint(symbol=ticker)

#     stock_price = data['05. price']

#     return stock_price

# @app.route('/stock-price', methods=['POST'])
# def stock_price():
#     ticker = request.json['ticker']
#     stock_price = get_alpha_vantage_stock_price(ticker)

#     return jsonify({'ticker': ticker, 'stock_price': stock_price})


