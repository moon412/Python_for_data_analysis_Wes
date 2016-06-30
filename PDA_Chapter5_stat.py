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
df.idxman()
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

