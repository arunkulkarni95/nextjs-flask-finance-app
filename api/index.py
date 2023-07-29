from flask import Flask
from routes.stock_price import stock_price_bp
from routes.assets import assets_bp
from routes.liabilities import liabilities_bp
from routes.net_income import net_income_bp
from routes.shares_outstanding import shares_outstanding_bp
from routes.all_company_concepts import all_company_concepts_bp
import logging
import sys

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

# Register blueprints
app.register_blueprint(stock_price_bp, url_prefix='/api')
app.register_blueprint(assets_bp, url_prefix='/api')
app.register_blueprint(liabilities_bp, url_prefix='/api')
app.register_blueprint(net_income_bp, url_prefix='/api')
app.register_blueprint(shares_outstanding_bp, url_prefix='/api')
app.register_blueprint(all_company_concepts_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()
