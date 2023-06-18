# Quiz 1. Understand Quantitative Strategies

Q1. If you believe that the price and volume history of an asset are all that is needed to design a trading strategy then you would would use an endogenous trading rule. What is the theoretical justification for using this type of strategy?
- _Fundamental data such as historic earning and sales growth are already fully reflected in the current market price and so have no predictive power._
- _Asset and market prices tend to have momentum so that stocks whose prices are in an up trends tend to increase in value and those in a downtrend tend to decrease in value._
- Asset prices follow a random walk with equal probabilities of increasing and decreasing
- Markets are efficient and fully incorporate all available information (both public and private)

Q2. The basic trading model parameters are entry signal, profit exit, stop-loss and time-out. How can you use these parameters and machine learning to optimize your trading strategy?
- Vary the the type of entry signal and profit exit levels in backtesting with the objective of maximizing profit.
- _Vary the the type of entry signal, profit exit levels,  stop loss levels and trade completion time limits in backtesting with the objective of maximizing risk adjusted return (Sharpe ratio) within your tolerance for PnL volatility and maximum drawdown._
- Vary the the type of entry signal and profit exit levels in backtesting with the objective of maximizing risk adjusted return (Sharpe ratio).

Q3. The main benefit of a dynamic stop loss over a static stop loss is that:
- _Dynamic stop losses reduce the expected risk of your strategy._
- Dynamic stop losses increase your expected returns from a trading strategy.
- Dynamic stop losses guarantee that your strategy will not make a loss even if it is stopped out.

Q4. Endogenous trading rules are often created by:
- _Technical analysts_
- Statistical arbitrage traders
- Strategists
- Quantitative trading groups

# Quiz4. Pairs Trading Strategy concepts

Q1. What is the advantage of trading a long-short pair of stocks versus a single stock?
- _You can lower your exposure to industry and sector risk_
- _You exposure to market risk is lower_
- You double your expected return

Q2. A long-short pairs trade will have a positive return if:
- _The long side has a larger positive return than the short side._
- The long side has a smaller positive return than the short side
- _The long side has a smaller negative return than the short side._
- The long side has a larger negative return than the short side.

Q3. Your fundamental and statistical research indicate that Oracle (ORCL) will outperform Salesforce (CRM) over the next quarter. Oracle is currently trading at $50 and has a beta of 1.15. Salesforce is trading at $165 and has a beta of 1.22. You have total trading capital of $10,000,000 and your risk management team say you can can only allocate 5% to each strategy. If you fully allocate to a long ORCL, short CRM pair, how many shares of CRM should you short if you want the strategy to be beta hedged?
- 3,030 shares of Salesforce (CRM)
- _2,856 shares of Salesforce (CRM)_
- 2,484 shares of Salesforce (CRM)

Q4. When we ran a principal components analysis of the 68 stocks in the XLK Technology ETF, our first component, PC1 explained a little over 50% of the variation in returns for the XLK stocks. All of the stocks had positive loadings in PC1. Why did we chose a pair of stocks that had equal loadings in this dimension?
- We wanted to create a long-short pair of to stocks in the same industry sub-sector and equal loadings in PC1 indicate that the stocks are in the same sub-sector.
- We wanted to create a long-short pair of to stocks with the same price/earnings ratio which is one way to measure the Value factor. 
- _We wanted to create a long-short pair of stocks that were hedged in their main exposure to variations in the overall returns of the XLK portfolio of stocks._

Q5. You have backtested 10 trading strategies using two distinct data sets representing different market regimes (down-trending with high volatility and up-trending with low volatility). From the 10 strategies you have identified the ones with the highest Sharpe ratio and highest return under each regime. 

| Strategy | Return | PnL Vol | Sharpe Ratio | Regime    |
|----------|--------|---------|--------------|-----------|
| 3        | 0.08   | 0.04    | 2            | Down/High |
| 6        | 0.05   | 0.02    | 2.5          | Up/Low    |
| 7        | 0.1    | 0.06    | 1.67         | Down/High |
| 10       | 0.06   | 0.03    | 2            | Up/Low    |

The strategies have about 70% pair-wise correlations with each other. Your analysis predicts a 75% chance that the market will be up-trending and low volatility and 25% chance that it will be down-trending and high volatility.  Which strategy or combination of strategies would you choose for implementation or further backtesting and why would you choose it or them?
- Implement Strategy 6 because it has the highest Sharpe ratio and it is the most likely market regime.
- Implement a  combination of Strategy 7 and 10 as this will give you the highest expected return regardless of the market regime.
- Implement a  combination of Strategy 3 and 6 as this will give you the highest expected Sharpe ratio regardless of the market regime.
- _Rather than looking at the performance of individual strategies, consider backtesting combinations of different strategies and determining the combination that gives you the highest Sharpe ratio._