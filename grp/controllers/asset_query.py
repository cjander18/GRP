from datetime import datetime

class AssetQuery:

    __baseUrl = "https://www.alphavantage.co/query"
    __dailyAdjustedParam = "function=TIME_SERIES_DAILY_ADJUSTED&datatype=json"
    __apiKey = "apikey=88G1Z95JM69VJ3Q7"

    def __init__(self, tickerQueryParam, dateQueryParam):
        queryUrl = ""

        symbol = self.getSymbolQueryParam(tickerQueryParam)
        parsedDate = self.parseDate(dateQueryParam)
        outputSize = self.getOutputSizeQueryParam(parsedDate)

        self.__setUrl([self.__apiKey, self.__dailyAdjustedParam, symbol, outputSize ])

    # Get the query URL
    @property
    def queryUrl(self):
        return self.__queryUrl

    # Set the query URL
    def __setUrl(self, queryParams):
        self.__queryUrl = "{0}?{1}".format(self.__baseUrl, "&".join(queryParams))

    # Convert a date
    @staticmethod
    def parseDate(dateValue):
        return datetime.strptime(dateValue, '%Y-%m-%d')

    # If the date is less than or equal to 100 days old output size is compact, else it's full
    @staticmethod
    def getOutputSizeQueryParam(dateValue):
        outputSize = 'compact' if ((datetime.now() - dateValue).days <= 100) else 'full'
        return "outputsize={0}".format(outputSize)

    # Get the symbol query parameter
    @staticmethod
    def getSymbolQueryParam(ticker):
        return "symbol={0}".format(ticker)

