from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

def parser(x):
	return datetime.strptime(x, '%Y-%m-%d %H')

series = read_csv('dates_and_values2.csv', parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
X = series.values
print(series.head())