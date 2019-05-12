import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
plt.style.use('ggplot')
start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()
df = web.DataReader("TSLA", 'yahoo', start, end)
df.to_csv('/Users/raunitsingh/Desktop/TSLA.csv')

df = pd.read_csv('/Users/raunitsingh/Desktop/TSLA.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

ax1 = plt.subplot2grid((df.shape[1], 1), (0, 0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((df.shape[1], 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)
ax1.plot(df.index, df['Adj Close'], color='c')
ax1.plot(df.index, df['100ma'], color='g')
ax2.bar(df.index, df['Volume'], color='y')
plt.savefig('basic.png')
plt.show()



