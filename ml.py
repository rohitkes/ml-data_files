import pandas as pd
import quandl as Quandl
import math

#import numpy as np
#from sklearn import preprocessing, cross_validation, svm
#from sklearn.linear_model import LeniarRegression

df = Quandl.get('WIKI/GOOGL')
df.to_csv('a.csv')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.0
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
'''
forecast_col = 'Adj. Close'
df.fillna(-99999,inplace=True)
forecost_out = int(math.ceil(0.01*len(df)))
df.dropna(inplace=True)
df['label'] = df[forecast_col].shift(-forecost_out)

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

X == preprocessing.scale(X)

#X = X[:-forecast_out+1]
df.dropna(inplace=True)
y = np.array(df['label'])

print (len(X))
'''
print df.head()
