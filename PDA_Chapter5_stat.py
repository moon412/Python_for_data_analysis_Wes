# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:02:57 2016

@author: yzhao03
Python for Data Analysis by Wes
Chapter 5
The second half: Statistics
"""

"""
Summarizing and Computing Descriptive Statistics
"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
df = DataFrame([[1.4, np.nan],
                [7.1, -4.5],
                [np.nan, np.nan],
                [0.75, -1.3]],
                index=['a', 'b', 'c', 'd'],
                columns=['one', 'two'])
df.sum() 
df.sum(axis=1) #sum along axis=1, columns 
df.mean(axis=1, skipna=False)
df.idxmax()
df.idxmin(axis=1)              
df.cumsum()
df.describe()
obj = Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()
df['three'] = ['a','b','c','a']
df.describe()
df['three'].describe()

"""
Correlation and Covariance
"""
import pandas.io.data as web
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
price = DataFrame({tic: data['Adj Close'] 
                   for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume']
                   for tic, data in all_data.iteritems()})        
returns = price.pct_change()                   
returns.tail()
returns.MSFT.corr(returns.IBM)
returns.MSFT.cov(returns.IBM)
returns.corr()
returns.cov()
returns.corrwith(returns.IBM)
returns.corrwith(volume)

"""
Unique Values, Value Count, and Membership
"""
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
obj.value_counts()
pd.value_counts(obj.values)
pd.value_counts(obj.values, sort=False)
mask = obj.isin(['b', 'c'])
obj[mask]
data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
data.apply(pd.value_counts).fillna(0) 

"""
Handling Missing Data
06/30/2016
"""
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])     
string_data.isnull()            
string_data[0] = None
string_data.isnull()

"""
Filtering Out Missing Data
"""
from numpy import nan as NA
data = Series([1, NA, 3.5, NA, 7])
data.dropna()
data[data.notnull()]
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
data.dropna(how='all')
data.dropna(axis=1, how='all')
data[4]= NA
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
df.dropna(thresh=3)

"""
Filling in Missing Data
"""
df.fillna(0)
df.fillna({1: 0.5, 3: -1})
#Always returns a  reference to the filled object
_ = df.fillna(0, inplace=True)
df = DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA
df.ix[4:, 2] = NA
df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)
data = Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())

"""
Hierarchical Indexing
"""
data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data.index                    
data['b']
data['b':'c']
data.ix[['b', 'd']] 
data.loc[['b', 'd']]
data[:, 2]
data.unstack()
data.unstack().stack()
frame = DataFrame(np.arange(12).reshape(4, 3),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2'] 
frame.columns.names = ['state', 'color'] 
frame['Ohio']
new_columns=pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
                       names=['state', 'color'])

"""
Reordering and Sorting Levels
"""
frame.swaplevel('key1', 'key2')
frame.sortlevel(1) #What is the difference from DataFrame.sort_index
frame.swaplevel(0, 1).sortlevel(1) 

"""
Summary Statistics by Level
"""
frame.sum(level='key2')
frame.sum(level='color', axis=1)

"""
Using a DataFrame's columns
"""
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
frame.set_index(['c', 'd'])
frame.set_index(['c', 'd'], drop=False)
frame.reset_index()

"""
Other pandas Topics
Integer indexing
"""
ser = Series(np.arange(3.))
ser[-1] #Erroe because cannot distinguish label or position
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1] #no error, label is string, this should be position
ser3 = Series(range(3), index=[-5, 1, 3])
ser3.iget_value(2)
ser3.iloc[2]
frame = DataFrame(np.arange(6).reshape((3, 2)), index=[2, 0, 1])
frame.irow(0)
frame.iloc[0]

"""
Panel Data
a dict of DataFrame objects or a 3-D ndarray
"""
import pandas.io.data as web
pdata = pd.Panel({stk: web.get_data_yahoo(stk, '1/1/2009', '6/1/2012')
                 for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']})
pdata2 = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009', '6/1/2012'))
                        for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']))
pdata = pdata.swapaxes('items', 'minor')
pdata.ix[:, '6/1/2012', :]
pdata.ix['Adj Close', '5/22/2012':, :]
stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
pdata.ix['Open':'High', :, :].to_frame()
