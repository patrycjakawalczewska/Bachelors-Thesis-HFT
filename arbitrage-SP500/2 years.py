#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
data = yf.download(['SPY', 'ES=F'], period='2y', interval='1wk', group_by='ticker')


#specify the data
PeriodStart = "2021-03-01"
PeriodEnd  = "2023-03-05"
tickerlist = ["ES=F", "SPY"]

#download the data
df = yf.download(tickerlist, start = PeriodStart, end = PeriodEnd)['Adj Close']
df.head()


#create a chart with different x axis, but the same y axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
line1 = ax.plot(df['ES=F'], label = "ES=F", color = "green")
ax2 = ax.twinx()
line2 = ax2.plot(df['SPY'], label = "SPY", color = "blue")

#add the second variable to the labels
lines = line1 + line2
labels = [1.get_label() for 1 in lines]
lines = line1 + line2
labels = [line.get_label() for line in lines]
ax.legend(lines, labels, loc=0)

#set the title and label axis
plt.title('(a) 2 years')
ax.grid()
ax.set_xlabel('Time (CT)')
ax.set_ylabel('Index Points (ES=F)')
ax2.set_ylabel('Index Points (SPY)')

#display the graph
plt.show()
