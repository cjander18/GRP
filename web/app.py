from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_whale():
    return render_template("whale_hello.html")

# Used https://www.alphavantage.co/documentation/#dailyadj API
#
# Example call: http://localhost:5000/asset?ticker=VOO&date=2020-02-14
@app.route('/asset', methods=['GET'])
def get_asset_data():
    ticker = request.args.get('ticker')
    dateStr = request.args.get('date')
    date = datetime.strptime(dateStr, '%Y-%m-%d')
    outputSize = 'compact' if ((datetime.now() - date).days <= 100) else 'full'
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&apikey=88G1Z95JM69VJ3Q7&outputsize={1}&atatype=json".format(ticker, outputSize))
    print(response.json())
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
