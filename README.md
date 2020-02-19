## Geometric returns Rebalancing often Portfolio (GRP)

### Getting Started

From the top level directory (i.e. where the docker-compose.yml file lives) run:

```
docker-compose build grp
docker-compose up grp
```

Go to http://localhost:5000

### Rebalancing

Rebalance weekly (too expensive when portfolio < 300k)

### Portfolio

- 20YR Treasuries: TLT
- Gold: BAR
- S&P 500: VOO
- Cash

### Phase 1 (Individual assets)

- Getting the data -> independent of all else, return arithmetic average and standard dev of asset. Alpha vantage?
  - TLT/BAR/VOO can all be the same API endpoint (API gateway -> Lambda) called 3 separate times with each ticker
  - Cash might need its own API endpoint (API gateway -> Lambda) b/c it requires the 3 mo t-bill yield

#### Details

- Get last 30 days of price data
- Subtract close price from open price, this is returns for the day
- Arithmetic average (mean) these returns
- Get the std dev = For each average, subtract the mean and square the result. Get the mean of those results. Square root it all. Done.

- risk free rate (rate of return to use for cash) = yield of the 3 month T-bill

### Phase 2 (Portfolio construction)

- Making the calculations
  - Central FLASK app (can be nested in an API gateway call to a Lambda)

#### Details

portfolioArithmeticMean = assetOnePortfolioAllocation _ assetOneMean + assetTwoPortfolioAllocation _ assetTwoMean + ....
portfolioStdDev = ((assetOnePortfolioAllocation ** 2) \* (assetOneStdDev ** 2) + (assetTwoPortfolioAllocation ** 2) \* (assetTwoStdDev ** 2) + ...) \*\* 1/2
geometric return = (portfolioArithmeticMean - portfolioStdDev) / 2 -> Maximize this!

Whatever maximizes the geometric returns will tell you the asset allocation between TLT, BAR, VOO, and cash.

### Phase 3 (Portfolio execution)

- Executing the position updates
  - One API endpoint (API gateway -> Lambda) to buy/sell TLT/BAR/VOO

#### Details

turtles candles trees...
