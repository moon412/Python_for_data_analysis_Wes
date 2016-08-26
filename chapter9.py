# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:02:09 2016
Chapter 9 Data Aggregation and Group Operations

@author: yzhao03
"""
import pandas as pd
import numpy as np
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

