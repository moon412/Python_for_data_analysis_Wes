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
