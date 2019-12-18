import pandas as pd
from pandas import datetime
from matplotlib import pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

#PM_10 = pd.read_csv('C:/Users/Tehnic/PycharmProjects/Implementing_ARIMA/dates_and_values.csv', index_col=0, parse_dates=[0], date_parser=parser)
PM_10 = pd.read_csv('C:/Users/Tehnic/PycharmProjects/Implementing_ARIMA/dates_and_values.csv')

print(PM_10[1])




