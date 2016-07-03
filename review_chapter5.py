# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 09:43:24 2016

@author: yzhao03
Review on Chapter 5
"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series(np.random.randn(10), index=list('abcdefghij'))
obj.index.name = 'key'
obj['a':'f']
obj[0:6]
obj.loc[['a', 'c', 'g']]
obj.ix[1:6]
obj.shape
obj.reindex(['f', 'd', 'z'])
obj['z'] = 4
obj.mean()
obj.idxmin() #how to return an integer position?
obj.index = np.arange(len(obj.index))
obj.idxmax()
obj.sort_index()
obj.sort_values()
obj[obj > 0]
obj.ix[['d', 'f', 'j']] = np.nan
obj[obj.notnull()]
obj.dropna()
obj.fillna(0)
obj.fillna(method='bfill')
obj2 = Series({'a': 1, 'b': 3, 'f': 5, 'g': 7,
               'f':9, 'h': 10, 'x': 11, 'y':12, 'z':10})
obj + obj2
obj + obj2.sort_index()
obj3 = Series(np.random.randn(11),
              index=[list('aaacccxxyyd'), [1,2,4,1,3,2,1,2,3,1,3]])
obj3['a']
obj3.ix[['a', 'c']]
obj3['x', 2]
obj3.sort_index(level=0)
obj3.sort_index(level=1)
obj3.sort_values()
obj3.sortlevel(1)
obj3.swaplevel(0,1)
obj3.mean()
obj3.mean(level=1)
obj3.unstack()

frame = DataFrame(np.random.randn(15).reshape((5, 3)),
                  index=['a', 'b', 'c', 'd', 'e'],
                  columns=['Washu', 'STL', 'UM'])
frame.shape
frame.index
frame.columns
frame['Washu']
frame[0:3]
frame.loc['a':'d', 'STL':]
frame.iloc[0:3, 1:2]
frame['UMST'] = 4
frame.reindex(index=['c', 'e', 'a'], columns=['UM', 'Washu'])
frame[frame < 0] = np.nan
frame.isnull()
frame.dropna()
frame.dropna(axis=1)
um = frame['UM']
um[um.notnull()]
frame.fillna(method='ffill', axis=0, limit=1, inplace=False)
frame.fillna(method='ffill', axis=1, limit=1)
frame.mean()
frame.mean(axis=1, skipna=False)
frame.idxmin()
frame.idxmax(axis=1)
frame2 = DataFrame({'Washu': np.random.randn(5),
                    'UM': np.random.randn(5),
                    'UMST': np.random.randn(5)},
                    index=list('abcde'))
frame3 = DataFrame({'a': {'Washu': 1, 'UM': 3},
                    'b': {'Washu': 2, 'UM': 4},
                    'd': {'Washu': 3, 'UM': 4}})
frame3 = frame3.T
frame + frame2
frame - frame3
d = frame.to_dict()
DataFrame(d)
frame4 = DataFrame({'a': np.random.randn(4),
                    'b': ['foo', 'lol'] * 2,
                    'c': [True, False] * 2},
                    index = list('abcd'))
frame.ix['f'] = np.random.randn(4)
frame['loc'] = ['ST', 'MO'] * 3
frame.sort_index(axis=1)
frame.sort_values(by=['loc', 'STL'])
frame.rank(axis=0)
frame.rank(method='max')
um.order()
um.rank()
frame.add(frame2)
frame.corr(um)
frame.fillna(1, inplace='True')
um = frame['UM']
frame.corr()
frame.cov()
frame2.ix['f'] = np.random.randn(3)
frame.corrwith(frame2) #corrwith a Series???
frame.corrwith(um) # error to corrwith a Series
frame.corrwith(um.to_frame())
frame.ix[:, 'Washu':'UMST'].apply(lambda x: x.mean())
frame.set_index('UM', drop=True, inplace=True)
keys = frame.index
frame.reset_index(level=keys)

df = DataFrame(np.random.randn(6, 5),
               columns=['Ohio', 'Dallas', 'Michigan', 'Miami', 'DC'],
               index=[['a', 'a', 'b', 'b', 'c', 'd'], [1,2,3,1,2,3]])
df.index
df.ix['a']
df.sortlevel(level=0, axis=0)
df.sortlevel(level=1, axis=0)
df.swaplevel(0, 1)
df_unstack = df.swaplevel(0, 1).unstack() #turn the column into Multiindex

import pandas.io.data as web
data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
p = pd.Panel(data)
p2 = p.swapaxes('items', 'major')

"""
Extra
"""
obj.values
np.exp(obj)
'b' in obj
pd.isnull(obj)
frame2['STL'] = [2, 3, 4] # Error
frame2['STL'] = Series([2, 3, 4], ['a', 'b', 'e'])
del frame2['STL']
DataFrame({'a': Series([1, 2, 3]),
           'b': Series(['John', 'Amy', 'Mark']),
           'c': Series([True, False, True])})
DataFrame([Series([1, 2, 3]),
          Series(['John', 'Amy', 'Mark']),
          Series([True, False, True])])
DataFrame([[1, 2, 3],
           ['J', 'A', 'M'],
           [True, False, True]])
'c' in frame2.index
'Washu' in frame2.columns
'Washu' in frame2
frame2.drop('d')
frame2.drop('Washu', axis=1)
frame2[frame2['Washu'] > 0]
frame2 = frame2.fillna(0)
frame2.ix[frame2.Washu > 0, frame2.ix['d'] > 0]
frame2.xs('d')
frame2.xs('UM', axis=1)
frame2.icol(2)
frame2.irow(4)
frame2.add(frame3, fill_value=0)
frame2.applymap(lambda x: '%.2f' % x)
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df.index.is_unique
df.index.unique()
df.ix['a']
frame2.describe()
"""
Unique values, value counts, membership
Not unique indices
"""
obj = Series(list('cbdaabbcc'))
obj.unique()
obj.value_counts()