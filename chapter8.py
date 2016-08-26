# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 00:33:08 2016

@author: yue
Chapter 8 Plotting and Visualization
"""
import numpy as np
from pylab import * #equal to ipython --pylab
plot(np.arange(10)) #test
import matplotlib.pyplot as plt
"""
Figures and Subplots
"""
fig = plt.figure(1, figsize=(8, 6))
fig2 = plt.figure(2, figsize=(6, 4))
plt.gcf()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))
fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
#adjusting the spacing around subplots
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)    

"""
Colors, Markers, and Line Style
"""
fig = plt.figure(1)
ax = fig.add_subplot(2,2,1)
x, y = np.random.randn(10), np.random.randn(10)
ax.plot(x, y, 'g--')
ax2 = fig.add_subplot(2,2,2)
ax2.plot(x, y, linestyle='--', color='g')
ax3 = fig.add_subplot(2,2,3)
ax3.plot(x, y, 'ko--')
ax4 = fig.add_subplot(2,2,4)
ax4.plot(np.random.randn(30).cumsum(), 'ko--')
ax4.get_xlim()
ax4.get_xticks()
ax4.set_xlim([0, 40])
ax.plot(np.random.randn(30).cumsum(), linestyle='dashed', color='k', marker='o')
plt.plot(x, y, 'bo--')
plot(np.random.randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
data = np.random.randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'g--', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
"""
Ticks, labels, and legends
"""
plt.xlim()
plt.xlim([0, 50])
fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five', 'six'],
                            rotation=30, fontsize='small') #'six' doesn't show
ax.set_xlabel('Stages')
ax.set_title('My first matplotlib plot')
fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum(), 'k', label='one')
ax.plot(np.random.randn(1000).cumsum(), 'k--', label='two')
ax.plot(np.random.randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best')

"""
Annotations and Drawing on a Subplot
"""
import os
os.chdir('H:\Yue_backup\pydata-book')
#os.chdir('D:\courses\Python_for_data_analysis')
from datetime import datetime
import pandas as pd
data = pd.read_csv('ch08/spx.csv', index_col=0, parse_dates=True)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
spx = data['SPX']
spx.plot(ax=ax, style='k')
ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title('Important dates in 2008-2009 financial crisis')
crisis_data = [(datetime(2007, 10, 11), 'Peak of bull market'),
               (datetime(2008, 3, 12), 'Bear Stearns Fails'),
               (datetime(2008, 9, 15), 'Lehman Bankruptcy')]

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 100),
                xytext=(date, spx.asof(date) + 200),
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left', verticalalignment='top')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
                   color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)

"""
Plotting Functions in pandas
"""
"""
Line plots
"""
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
               columns=['A', 'B', 'C', 'D'],
               index=np.arange(0, 100, 10))
df.plot()    

"""
Bar plots
"""
fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)
df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot(kind='bar')
df.plot(kind='barh', stacked=True)
tips = pd.read_csv('ch08/tips.csv')
party_counts = pd.crosstab(index=tips.day, columns=tips['size'])           
party_counts = party_counts.ix[:, 2:5]
party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)
#pandas.DataFrame.sum(axis) sum along which axis, sum the numbers on which axis
#pandas.DataFrame.divide(axis): divide the number along wich axis
party_counts.divide([10,100,1000,10000], axis=0)               
party_pcts.plot(kind='bar', stacked=True)   

"""
Histograms and Density Plots
"""
tips['tip_pct'] = tips['tip']/tips['total_bill']      
tips['tip_pct'].hist(bins=50)    
tips['tip_pct'].plot(kind='hist', bins=50)      
tips['tip_pct'].plot(kind='kde')
comp1 = np.random.normal(0, 1, size=200) #N(0, 1)
comp2 = np.random.normal(10, 2, size=200) #N(10, 4)
values = pd.Series(np.concatenate([comp1, comp2]))
values.hist(bins=100, alphs=0.3, color='k', normed=True)
values.plot(kind='kde', style='k--')
"""
Scatter Plots
"""
macro = pd.read_csv('ch08/macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
plt.scatter(trans_data['m1'], trans_data['unemp'])
plt.title('Changes in log %s vs. log %s' % ('m1', 'unemp'))
pd.scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3)
"""
Plotting Maps: Visualizing Haiti Earthquake Crisis Data
"""
data = pd.read_csv('ch08/Haiti.csv')
data[['INCIDENT DATE', 'LATITUDE', 'LONGITUDE']][:10]
data['CATEGORY'][:6]
data = data[(data.LATITUDE > 18) & (data.LATITUDE < 20) &
            (data.LONGITUDE > -75) & (data.LONGITUDE < -70) &
            data.CATEGORY.notnull()]
def get_english(cat):
    """
    cat is one category
    return the code and English content
    """
    code, names = cat.split('.')
    if '|' in names:
        names = names.split('|')[1]
    return code, names.strip()
    
def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]
    
def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
 
all_cats = get_all_categories(data.CATEGORY)
english_mapping = dict(get_english(x) for x in all_cats)

def get_code(seq):
    return [x.split('.')[0] for x in seq if x]
all_codes = get_code(all_cats)
import numpy as np
code_index = pd.Index(np.unique(all_codes))
dummy_frame = pd.DataFrame(np.zeros((len(data), len(code_index))), 
                           index=data.index, columns=code_index)   
for row, cat in zip(data.index, data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    dummy_frame.ix[row, codes] = 1
data = data.join(dummy_frame.add_prefix('category_'))

from mpl_toolkits.basemap import Basemap
    
