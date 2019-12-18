#SCP3_medii_orare_25oct_10feb


#https://www.youtube.com/watch?v=D9y6dcy0xK8

import pandas as pd
from pandas import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from statsmodels.tsa.arima_model import ARIMA
from pandas import read_csv
from pandas import datetime
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import math


dates, values = [], []
data = read_csv('SCP_rfc3339_medii_orare.csv')

start = int(137782)
stop = int(144553)

for row in data.iterrows():
    if int(row[0]) >= start and int(row[0]) < stop:
        if(row[1][2] != 'mean'):
            #print(row[1][1])
            #print(row[1][1][0:10], row[1][1][12:13])
            dates.append(row[1][1][0:10] + " " + row[1][1][11:13])
            #print(row[1][2])
            values.append(row[1][2])

#print(len(dates))
#print(len(values))


with open('dates_and_values2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(dates)):
        writer.writerow([dates[i], values[i]])
