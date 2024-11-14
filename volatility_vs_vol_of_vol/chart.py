import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

def save_close_prices_plot(df, filename='close_prices_image.png'):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['close'], label='Close Price', color='blue', alpha=0.5)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Close Prices')
    plt.legend()
    plt.savefig(filename)
    plt.close()

def chart_volatility_vs_vol_of_vol(df, close_prices_image='close_prices_image.png'):
    # Filter the last week of data for volatilities
    last_week_df = df.last('7D')

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot rolling volatility on the primary y-axis
    ax1.plot(last_week_df.index, last_week_df['rolling_volatility'], label='Rolling Volatility', color='orange')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Rolling Volatility', color='orange')
    ax1.tick_params(axis='y', labelcolor='orange')

    # Create a secondary y-axis for the volatility of volatility
    ax2 = ax1.twinx()
    ax2.plot(last_week_df.index, last_week_df['vol_of_vol'], label='Volatility of Volatility', color='green')
    ax2.set_ylabel('Volatility of Volatility', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    # Superimpose the close prices image
    img = Image.open(close_prices_image)
    fig.figimage(img, xo=50, yo=fig.bbox.ymax - img.size[1] - 50, alpha=0.5, zorder=1)

    # Add labels and legend
    fig.suptitle('Rolling Volatility and Volatility of Volatility with Close Prices')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

    plt.show()