# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:02:09 2016
Chapter 9 Data Aggregation and Group Operations

@author: yzhao03
"""
import pandas as pd
import numpy as np
"""
Groupby Mechanics
"""
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                'data1': np.random.randn(5),
                'data2': np.random.randn(5)})
grouped = df['data1'].groupby(df['key1'])
grouped.mean()
grouped_2 = df['data1'].groupby([df['key1'], df['key2']])
means = grouped_2.mean()
means.unstack()
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states, years]).mean()
df.groupby('key1').mean()
df.groupby(['key1', 'key2']).mean()
df.groupby(['key1', 'key2']).size()

"""
Iterating Over Games
"""
for name, group in df.groupby('key1'):
    print name
    print group
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print k1, k2
    print group
pieces = dict(list(df.groupby('key1')))
list(df.groupby(['key1', 'key2']))
grouped = df.groupby(df.dtypes, axis = 1)
dict(list(grouped))

"""
Selecting a Column or Subset of Columns
"""
df.groupby('key1')['data1']
df.groupby('key1')[['data1']]
df['data1'].groupby(df['key1'])
df[['data1']].groupby(df['key1'])
df.groupby(['key1', 'key2'])[['data2']].mean()

"""
Grouping with Dicts and Series
"""
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.ix[2:3, ['b', 'c']] = np.nan
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}
by_column = people.groupby(mapping, axis=1)
by_column.sum()  
people.groupby(['red', 'red', 'blue', 'blue', 'red'], axis=1).mean() 
map_series = pd.Series(mapping)
people.groupby(map_series, axis=1).count()

"""
Grouping with Functions
"""
people.groupby(len).sum()
people.groupby(len, axis=1).sum()
key_list = ['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min()

"""
Group by Index Levels
"""
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
hier_df.groupby(level='cty', axis=1).count()

"""
Data Aggregation
"""
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)
def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped.agg(peak_to_peak)
grouped.describe()

import os
#os.chdir('/home/moon/pydata-book')
os.chdir('H:\Yue_backup\pydata-book')
tips = pd.read_csv('ch08/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')
grouped_pct.agg(['mean', 'std', peak_to_peak])
grouped_pct.agg([('foo', 'mean'), ('bar', np.std)])
functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
grouped['tip_pct', 'total_bill'].agg(ftuples)
grouped.agg({'tip': np.max, 'size': 'sum'})
grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'],
             'size': 'sum'})

"""
Returning Aggregated Data in "unindexed" Form
"""
tips.groupby(['sex', 'smoker'], as_index=False).mean()
grouped_2 = tips.groupby(['sex', 'smoker'], as_index=False)
grouped_2.mean()
grouped_2.agg({'tip_pct': ['mean', 'min'],
               'total_bill': 'sum'})
grouped_2['tip_pct', 'total_bill'].agg([('foo', 'mean'),
                                        ('bar', np.std)])
grouped_2.agg([('foo', 'mean'), ('bar', np.std)])
grouped_2.agg(['mean', 'std'])

"""
Group-wise Operations and Transformations
"""
k1_means = df.groupby('key1').mean().add_prefix('mean_')
pd.merge(df, k1_means, left_on='key1', right_index=True)

                                     


        