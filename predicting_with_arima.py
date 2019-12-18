from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

def parser(x):
	return datetime.strptime(x, '%Y-%m-%d %H')

series = read_csv('dates_and_values2.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
X = series.values
size = int(len(X) * 0.80)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(5,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot

pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()


test = np.array(test).ravel()
test = np.array(test)

predictions = np.array(predictions).ravel()
predictions = np.array(predictions)

corr_coef = np.corrcoef(test, predictions)[0,1]
print("corelatia: ",corr_coef)
