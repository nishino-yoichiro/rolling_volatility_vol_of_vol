import requests
import pandas as pd
import os

def load_data(ticker, timespan, from_date, to_date, api_key, csv_file, update=False):
    if not os.path.exists(csv_file) or update:
        url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/{timespan}/{from_date}/{to_date}?apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['results'])
        df.to_csv(csv_file)
    else:
        df = pd.read_csv(csv_file)

    df['date'] = pd.to_datetime(df['t'], unit='ms')
    df.set_index('date', inplace=True)

    return df

def get_rolling_volatility(df, rolling_window):
    df['close'] = df['c']
    df['returns'] = df['close'].pct_change()
    df['rolling_volatility'] = df['returns'].rolling(window=rolling_window).std()

    return df

def get_vol_of_vol(df, rolling_window):
    df['vol_of_vol'] = df['rolling_volatility'].rolling(window=rolling_window).std()

    return df