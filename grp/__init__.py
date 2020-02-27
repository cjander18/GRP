import warnings
import requests

from flask import Flask, render_template, request

from . import controllers
from .controllers import AssetQuery

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    @app.route('/')
    def hello_whale():
        return render_template("whale_hello.html")

    # Used https://www.alphavantage.co/documentation/#dailyadj API
    #
    # Example call: http://localhost:5000/asset?ticker=VOO&date=2020-02-14
    @app.route('/asset', methods=['GET'])
    def get_asset_data():
        tickerQueryParam = request.args.get('ticker', type=str)
        dateQueryParam = request.args.get('date', type=str)

        assetQuery = AssetQuery(tickerQueryParam, dateQueryParam)

        response = requests.get(assetQuery.queryUrl)
        print(response.json())
        return response.json()

    return app

app = create_app()
