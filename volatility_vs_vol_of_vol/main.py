from dotenv import load_dotenv
import os
from query import load_data, get_rolling_volatility, get_vol_of_vol

load_dotenv()

api_key = os.getenv('API_KEY')
symbol = 'SPY'
timespan = 'day'
from_date = '2022-01-01'
to_date = '2024-11-14'
csv_file = 'data/SPY.csv'
rolling_window = 20

df = load_data(symbol, timespan, from_date, to_date, api_key, csv_file)
get_rolling_volatility(df, rolling_window)
get_vol_of_vol(df, rolling_window)

