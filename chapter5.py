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
frame2['state']
frame2.year             
frame2.ix['three']      
frame2.debt = 16.5
frame2['debt'] = np.arange(5.)
frame2.debt = 'NaN'
val = Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
frame2['debt'] = val
frame2['eastern'] = frame2.state == 'Ohio'
del frame2['eastern']
frame2.columns
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002:3.6}}
frame3 = DataFrame(pop)       
frame3.T
DataFrame(pop, index=[2001, 2002, 2003])
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
DataFrame(pdata) 
frame3.index.name='year'
frame3.columns.name='state'      
frame3.values  
frame2.values
ldata = [frame3['Ohio'], frame3['Ohio']]
DataFrame(ldata)

"""
Index Objects
"""
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index[1:]
index[1] = 'd'
# pd.Index object is immutable !!!
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
obj2.index is index
#column is also Index object
frame3
frame3.columns
'Ohio' in frame3.columns
2003 in frame3.index

"""
Essential Functionality
Reindexing
"""
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='ffill')
frame = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
states = ['Texas', 'Utah', 'California']
frame.reindex(index=['a', 'b', 'c', 'd'], columns=states, method='ffill')
frame.ix[['a', 'b', 'c', 'd'], states]

"""
Dropping entries from an axis
"""
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c') #del is in place
obj.drop(['d', 'b'])
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data.drop(['Colorado', 'Ohio'])
data.drop('two', axis=1) 
       
"""
Indexing, selection, and filtering
"""
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj['b']
obj[1]
obj[2:4]
obj[['b', 'a', 'd']]
obj[[1, 3]]
obj[obj < 2]
obj['b':'c']
obj['b':'c'] = 5
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data['two']
data[['three', 'one']] #label indexing the columns
data[0:2]             #position slicing the rows
data[data['three'] > 5] #boolean selecting the rows
data[data<5] = 0
data.ix['Colorado', ['two', 'three']] #label indexing on the rows
data.ix[['Colorado', 'Utah'], [3, 0, 1]]
data.ix[2]
data.ix[:'Utah', 'two']
data.ix[data.three > 5, :3]

"""
Arithmetic and data alignment
"""
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1 + s2
df1 = DataFrame(np.arange(9.).reshape(3, 3),
                columns=['b', 'c', 'd'],
                index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)),
                columns=['b', 'd', 'e'],
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1 + df2

"""
Arithmetic method with fill values
"""
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1 + df2
df1.add(df2, fill_value = 0)
df1.reindex(columns=df2.columns, fill_value=0)

"""
Operations between DataFrame and Series
"""
arr = np.arange(12.).reshape((3, 4))
arr - arr[0]
frame = DataFrame(np.arange(12.).reshape((4, 3)),
                  columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.ix[0]             
frame - series     
series2 = Series(range(3), index=['b', 'e', 'f'])
frame + series2
frame - series2
series3 = frame['d']
frame.sub(series3, axis=0)

"""
Function application and mapping
"""
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
np.abs(frame)
f = lambda x: x.max()-x.min() 
frame.apply(f)     
frame.max() - frame.min()
frame.apply(f, axis=1)             
frame.max(axis=1) - frame.min(axis=1)
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)               
f = lambda x: '%.2f' % x
frame.applymap(f)
frame['e'].map(f)

"""
Sorting and ranking
"""
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_index(axis=1, ascending=False)    
obj = Series([4, 7, -3, 2])
obj.order()   
obj = Series([4, np.nan, 7, np.nan, -3, 2])
obj.order()
frame = DataFrame({'b':[4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame.sort_index(by='b')
frame.sort_index(by=['a', 'b'])
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()
obj.rank(method = 'first')      
obj.rank(ascending=False, method='first')     
obj.rank(ascending=False, method='max')
frame = DataFrame({'b': [4.3, 7, -3, 2],
                   'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
frame.rank()                   
frame.rank(axis=1)                 

"""
Axis indexes with duplicate values
"""
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj.index.is_unique         
obj['a']
obj['c']
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df.ix['a']

                 

