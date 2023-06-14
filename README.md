# Bachelor's thesis notes on HFT

This repository includes code used to visualise the findings in Python and Matlab. 
The empirical design is separated into 2 sections: arbitrage and transaction costs.

## Arbitrage - S&P500

This section intends to show the price discrepancies between two tickers (ES=F, SPY) following the same index S&P 500.
The lower the latency, the greater opportunities there are to exploit the price differences by applying arbitrage method.
By buying an ETF (SPDR S&P 500 ETF Trust (SPY)) on NYSE, and selling the future contract (E-Mini S&P 500 (ES=F)) at almost the same time (differrence in milliseconds), the trader can generate alpha and gain profit relative to the size of money invested.


## Transaction costs
