from config.config import Config
from alpha_vantage.timeseries import TimeSeries

def get_alpha_vantage_stock_price(ticker):
    api_key = Config.ALPHA_VANTAGE_API_KEY

    ts = TimeSeries(key=api_key, output_format='json')
    data, _ = ts.get_quote_endpoint(symbol=ticker)

    stock_price = data['05. price']

    return stock_price