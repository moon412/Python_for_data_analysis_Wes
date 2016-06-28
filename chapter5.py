# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 07:06:43 2016

@author: yue
Chapter 5
Getting Started with pandas
"""
"""
Series
"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
obj = Series([4, 7, -5, 3])
obj.values
obj.index
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2.index
obj2['a']
obj2['d'] = 6
obj2[['c', 'a', 'd']]
obj2
obj2[obj2 > 0]
obj2*2
np.exp(obj2)
'b' in obj2
'e' in obj2
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon':16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3
states = {'California', 'Ohio', 'Oregon', 'Texas'}
obj4 = Series(sdata, index=states)
obj4
pd.isnull(obj4)
pd.notnull(obj4)
obj4.isnull()
obj3
obj4
obj3 + obj4
obj4.name = 'population'
obj4.index.name = 'state'
obj4
obj
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

"""
DataFrame
"""
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame
DataFrame(data, columns=['year', 'state', 'pop'])
frame2 = DataFrame(data, columns = ['year', 'state', 'pop', 'debt'],
                   index = ['one', 'two', 'three', 'four', 'five'])
                   