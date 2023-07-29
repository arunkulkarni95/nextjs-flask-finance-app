from flask import Flask
from routes.stock_price import stock_price_bp
from routes.company_concepts import company_concepts_bp
import logging
import sys

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

# Register blueprints
app.register_blueprint(stock_price_bp, url_prefix='/api')
app.register_blueprint(company_concepts_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()
