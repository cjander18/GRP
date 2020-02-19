from flask import Flask, render_template, request
from datetime import datetime
import requests

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    def constructGetAssetUrl(tickerQueryParam, dateQueryParam):
        getDailyAdjustedUrl = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey=88G1Z95JM69VJ3Q7&datatype=json"
        parsedDate = datetime.strptime(dateQueryParam, '%Y-%m-%d')
        outputSize = 'compact' if ((datetime.now() - parsedDate).days <= 100) else 'full'
        return getDailyAdjustedUrl + "&symbol={0}&outputsize={1}".format(ticker, outputSize)

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
        response = requests.get(constructGetAssetUrl(tickerQueryParam, dateQueryParam))
        print(response.json())
        return response.json()

    return app

app = create_app()
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
