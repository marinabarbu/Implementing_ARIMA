#https://www.youtube.com/watch?v=D9y6dcy0xK8

import pandas as pd
from pandas import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def parser(x):
    return datetime.strptime(x, '%d %m %Y %H')

dates, values = [], []

data = pd.read_csv('C:/Users/Tehnic/PycharmProjects/Implementing_ARIMA/medii_pe_ore.csv')
for row in data.itertuples():
    #print(row[1])
    items = row[1].split(";")
    if items[3] == "PM10":
        #print(items[0], items[1], items[5])
        #print(parser(items[0]+" "+items[1]))
        dates.append(parser(items[0]+" "+items[1]))
        values.append(float(items[5]))

#print(dates)
#print(values)

dates_to_plot = mdates.date2num(dates)
plt.plot(dates_to_plot, values)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%Y-%m-%d %H')
plt.gca().xaxis.set_major_formatter(myFmt)
#print(dates_to_plot)

plt.show()
plt.close()

