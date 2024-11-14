from dotenv import load_dotenv
import os
from query import load_data, get_rolling_volatility, get_vol_of_vol
from chart import chart_volatility_vs_vol_of_vol, save_close_prices_plot

load_dotenv()

api_key = os.getenv('API_KEY')
symbol = 'SPY'
timespan = 'minute'
from_date = '2023-11-14'
to_date = '2024-11-14'
csv_file = 'data/SPY.csv'
rolling_window = 5

df = load_data(symbol, 'minute', from_date, to_date, api_key, 'data/SPY_M.csv', update=False)
df = load_data(symbol, 'day', from_date, to_date, api_key, 'data/SPY_D.csv', update=False)
df = get_rolling_volatility(df, rolling_window)
df = get_vol_of_vol(df, rolling_window)

save_close_prices_plot(df)
chart_volatility_vs_vol_of_vol(df)

