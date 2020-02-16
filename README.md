## Geometric returns Rebalancing often Portfolio (GRP)

### Getting Started

```
docker build -t grp:latest .
docker run -d -p 5000:5000 grp
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

### Phase 2 (Portfolio construction)

- Making the calculations
  - Central FLASK app (can be nested in an API gateway call to a Lambda)

### Phase 3 (Portfolio execution)

- Executing the position updates
  - One API endpoint (API gateway -> Lambda) to buy/sell TLT/BAR/VOO

### Phase 1 (Individual assets)

- Get last 30 days of price data
- Subtract close price from open price, this is returns for the day
- Arithmetic average (mean) these returns
- Get the std dev = For each average, subtract the mean and square the result. Get the mean of those results. Square root it all. Done.

- risk free rate (rate of return to use for cash) = yield of the 3 month T-bill

### Phase 2 (Portfolio construction)

- Portfolio arithmetic mean: Asset allocation _ mean + Asset allocation _ mean + ....
- Portfolio std dev: Square root(asset allocation squared _ asset std dev squared + asset allocation squared _ asset std dev squared + ...)
- (Arithmetic mean of portfolio - portfolio std dev squared) / 2 = geometric return -> Maximize this
- Whatever maximizes the geometric returns will tell you the asset allocation between TLT, BAR, VOO, and cash
