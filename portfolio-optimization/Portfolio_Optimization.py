# Input stock symbol and allocation of the stocks in the portfolio.
porfolio_list = {'SHB': 100}

# Input time to get data
from_date = '2018-01-01'
to_date = '2023-02-07'

# Input Total Portfolio Value. (1 M$)
TPV = 1000000

# Number of Portfolio
NUM_PORTS = 20000

# --------------------------------------------------------------------------------------------------------------------------------
# WIFEED API KEY
API_KEY = ""
STOCK_DATA_URL = ""

# --------------------------------------------------------------------------------------------------------------------------------
# MAIN FUNCTIONS

# Check verified porfolio
if sum(porfolio_list.values()) != 100:
    print(
        f'Sum of porfolio isnt correct. Please re-check porfolio again: {porfolio_list} with total: {sum(porfolio_list.values())}%')
    exit()

# Library
import json
import urllib.request
from scipy.optimize import minimize
import warnings
from pandas import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

warnings.simplefilter('ignore')

# Close price dataframe
combine_close = pd.DataFrame()

for symbol, alloc in porfolio_list.items():
    print(f'Processing {symbol} from {from_date} to {to_date}...')
    symbol_url = STOCK_DATA_URL.format(API_KEY, symbol, from_date, to_date)
    r = urllib.request.urlopen(symbol_url)
    raw_stock = json.loads(r.read())
    raw_stock_df = pd.json_normalize(raw_stock)
    raw_stock_df['ngay'] = pd.to_datetime(
        raw_stock_df['ngay'], format="%Y-%m-%d").dt.date
    raw_stock_df.to_csv(f'{symbol}_{from_date}_{to_date}.csv')

    # Select columns
    # close_root: "Giá đóng cửa gốc"
    # close_adjust: "Giá đóng cửa điều chỉnh"
    tmp_stock_df = raw_stock_df[['ngay', 'close_root', 'close_adjust']]

    # Normed Return column has been added to the dataframe combine_close
    tmp_stock_df[f'{symbol}_Normed_Return'] = tmp_stock_df['close_adjust'] / \
        tmp_stock_df.iloc[0]['close_adjust']

    # Column ALLocation has been added with a view to calculate the allocation of the stocks in the portfolio.
    tmp_stock_df[f'{symbol}_Allocation'] = tmp_stock_df[f'{symbol}_Normed_Return'] * alloc

    # Position Values of all the stocks.
    tmp_stock_df[f'{symbol}_Position_Values'] = tmp_stock_df[f'{symbol}_Allocation'] * TPV

    # Change name of close column to stock symbol. close_root: "Giá đóng cửa gốc" close_adjust:
    tmp_stock_df = tmp_stock_df.rename(
        {'close_root': symbol+'_close_root'}, axis=1)
    tmp_stock_df = tmp_stock_df.rename(
        {'close_adjust': symbol+'_close_adjust'}, axis=1)

    if combine_close.shape[0] == 0:
        combine_close = tmp_stock_df
    else:
        combine_close = pd.merge(combine_close, tmp_stock_df,  how='outer', left_on=[
                                 'ngay'], right_on=['ngay'])

# --------------------------------------------------------------------------------------------------------------------------------
# Total Portfolio Value:
combine_close['Total_Position_Values'] = combine_close.filter(
    regex='_Position_Values').sum(1)
portfolio_value = combine_close.filter(regex='_Position_Values')
portfolio_value['ngay'] = combine_close['ngay']
portfolio_value = portfolio_value.set_index('ngay')

# --------------------------------------------------------------------------------------------------------------------------------
# Portfolio Statistics
print('Portfolio Statistics...')
# Daily_Return Value:
portfolio_value['Daily_Return'] = portfolio_value['Total_Position_Values'].pct_change(
    1)

# Cumulative return:
cumulative_return = 100 * \
    (portfolio_value['Total_Position_Values'].iat[-1] /
     portfolio_value['Total_Position_Values'].iat[0] - 1)
print(f'Our cumulative return is {cumulative_return} percent!')

mean = portfolio_value['Daily_Return'].mean()
print(f'Our mean daily return is {mean}')

std = portfolio_value['Daily_Return'].std()
print(f'Our standard deviation of daily returns is {std}')

# Sharpe Ratio
sharpe_ratio = portfolio_value['Daily_Return'].mean(
)/portfolio_value['Daily_Return'].std()
print(f'Annualized Sharpe Ratio is {(252**0.5)*sharpe_ratio}')

# --------------------------------------------------------------------------------------------------------------------------------
# Portfolio Optimization using Monte Carlo Simulation
print('Portfolio Optimization using Monte Carlo Simulation...')

# Log Returns vs Arithmetic Returns
stock_close_root = combine_close.filter(regex='_close_root')
stock_close_root['ngay'] = combine_close['ngay']
stock_close_root = stock_close_root.set_index('ngay')

log_ret = np.log(stock_close_root/stock_close_root.shift(1))

print(f'Calculate the log return mean of each stock:\n{log_ret.mean() * 252}')
print('Compute pairwise covariance of columns')
print(log_ret.cov()*252)

# --------------------------------------------------------------------------------------------------------------------------------
# Run random allocation
print('Run random allocation...')

all_weights = np.zeros((NUM_PORTS, len(porfolio_list)))
ret_arr = np.zeros(NUM_PORTS)
vol_arr = np.zeros(NUM_PORTS)
sharpe_arr = np.zeros(NUM_PORTS)

for ind in range(NUM_PORTS):
    # Create Random Weights
    weights = np.array(np.random.random(len(porfolio_list)))

    # Rebalance Weights
    weights = weights / np.sum(weights)

    # Save Weights
    all_weights[ind, :] = weights

    # Expected Return
    ret_arr[ind] = np.sum((log_ret.mean() * weights) * 252)

    # Expected Volatility
    vol_arr[ind] = np.sqrt(
        np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))

    # Sharpe Ratio
    sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]

max_sr_ret = ret_arr[sharpe_arr.argmax()]
max_sr_vol = vol_arr[sharpe_arr.argmax()]

min_sr_ret = ret_arr[sharpe_arr.argmin()]
min_sr_vol = vol_arr[sharpe_arr.argmin()]

print(f'Sharpe Ratio Max {sharpe_arr.max()}')
print(
    f'The weights of Sharpe Ratio corresponding  {all_weights[sharpe_arr.argmax(),:]}')

# --------------------------------------------------------------------------------------------------------------------------------
# Mathematical Optimization
print('Mathematical Optimization...')


# Return, volatility and sharpe ratio
def get_ret_vol_sr(weights):
    """
    Takes in weights and returns back an array of mean return, mean volatility and sharpe ratio
    """
    weights = np.array(weights)
    ret = np.sum(log_ret.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
    sr = ret/vol
    return np.array([ret, vol, sr])


# Negative Sharpe Ratio
def neg_sharpe(weights):
    return get_ret_vol_sr(weights)[2] * -1


# Contraints
def check_sum(weights):
    '''
    Returns 0 if sum of weights is 1.0
    '''
    return np.sum(weights) - 1


cons = ({'type': 'eq', 'fun': check_sum})

# 0-1 bounds for each weight
bounds = ([(0, 1) for weight in weights])

# Initial Guess (equal distribution)
n = len(weights)
init_guess = [1/n for weight in weights]

# Sequential Least SQuares Programming (SLSQP)
opt_results = minimize(neg_sharpe, init_guess,
                       method='SLSQP', bounds=bounds, constraints=cons)
print(f'Sequential Least SQuares Programming (SLSQP) {opt_results}')

# --------------------------------------------------------------------------------------------------------------------------------
# All Optimal Portfolios (Efficient Frontier)
print('All Optimal Portfolios...')

# Our returns go from 0 to somewhere along 0.3
# Create a linspace number of points to calculate x on
# Change 100 to a lower number for slower computers!
frontier_y = np.linspace(0, 0.3, 100)


def minimize_volatility(weights):
    return get_ret_vol_sr(weights)[1]


frontier_volatility = []

for possible_return in frontier_y:
    # function for return
    cons = ({'type': 'eq', 'fun': check_sum},
            {'type': 'eq', 'fun': lambda w: get_ret_vol_sr(w)[0] - possible_return})
    result = minimize(minimize_volatility, init_guess,
                      method='SLSQP', bounds=bounds, constraints=cons)
    frontier_volatility.append(result['fun'])

plt.figure(figsize=(15, 8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.plot(frontier_volatility, frontier_y, 'g--', linewidth=3)

# Add red dot for max SR
plt.scatter(max_sr_vol, max_sr_ret, c='red', s=80, edgecolors='red')
plt.scatter(min_sr_vol, min_sr_ret, c='red', s=50, edgecolors='blue')
plt.show()
