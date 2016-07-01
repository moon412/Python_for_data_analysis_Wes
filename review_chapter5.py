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
