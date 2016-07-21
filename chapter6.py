# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 21:04:40 2016

@author: yue
Chapter 6 Data Loading, Storage, and File Formats
"""
import os
os.getcwd()
os.chdir('D:\courses\Python_for_data_analysis')
!type ch06/ex1.csv
import pandas as pd
df = pd.read_csv('ch06/ex1.csv')
pd.read_table('ch06/ex1.csv', sep=',')
pd.read_csv('ch06/ex2.csv', header=None) #default column names
pd.read_csv('ch06/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('ch06/ex2.csv', names=names, index_col='message')
parsed=pd.read_csv('ch06/csv_mindex.csv', index_col=['key1', 'key2'])
list(open('ch06/ex3.txt'))
pd.read_table('ch06/ex3.txt', sep='\s+')
pd.read_csv('ch06/ex4.csv')
pd.read_csv('ch06/ex4.csv', skiprows=[0, 2, 3])
result = pd.read_csv('ch06/ex5.csv')
pd.isnull(result)
result.isnull()
pd.read_csv('ch06/ex5.csv', na_values=['two', 'one'])
setinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('ch06/ex5.csv', na_values=setinels)

"""
Reading Text Files in Pieces
"""
result = pd.read_csv('ch06/ex6.csv')
pd.read_csv('ch06/ex6.csv', nrows=5)
chunker = pd.read_csv('ch06/ex6.csv', chunksize=500)
tot=pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot=tot.order(ascending=False)    

"""
Writing data out to text format
"""
data = pd.read_csv('ch06/ex5.csv')
data.to_csv('ch06/out.csv')
data.to_csv(sys.stdout, sep='|')
data.to_csv(sys.stdout, na_rep='NULL')
data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
dates = pd.date_range('1/1/2000', periods=7)
import numpy as np
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('ch06/tseries.csv')
s = pd.read_csv('ch06/tseries.csv', index_col=[0], header=None)
#how to choose first column as index here ?
pd.Series.from_csv('ch06/tseries.csv', parse_dates=True)

"""
Manually Working with Delimited Formats
"""
pd.read_csv('ch06/ex7.csv') #Error
import csv
f = open('ch06/ex7.csv')
reader = csv.reader(f)
for line in reader:
    print line
lines = list(csv.reader(open('ch06/ex7.csv')))    
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
reader = csv.reader(f, dialect=my_dialect)
    