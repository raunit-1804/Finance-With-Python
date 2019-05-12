import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
from mpl_finance import candlestick_ohlc
import matplotlib.dates as date


plt.style.use('ggplot')

df = pd.read_csv('/Users/raunitsingh/Desktop/TSLA.csv', parse_dates=True, index_col=0)

#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(date.date2num)
print(df.head())
print(df_ohlc.head())
print(df_volume.head())
ax1 = plt.subplot2grid((df.shape[1], 1), (0, 0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((df.shape[1], 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g', colordown='r')
ax2.fill_between(df_volume.index.map(date.date2num), df_volume.values, 0, facecolors='c')
plt.savefig('Candlestick_ohlc.png')
plt.show()
