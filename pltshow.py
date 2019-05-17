import matplotlib as mpl
import matplotlib.gridspec as gridsec
import matplotlib.ticker as ticker
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def showfig():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    plt.show()

    xax = ax.xaxis
    yax = ax.yaxis

    print( 'fig.axes:', fig.axes, '\n')
    print( 'ax.xaxis:', xax )
    print( 'ax.yaxis:', yax, '\n' )
    print( 'ax.xaxis.majorTicks:', xax.majorTicks, '\n' )
    print( 'ax.yaxis.majorTicks:', yax.majorTicks, '\n')
    print( 'ax.xaxis.minorTicks:', xax.minorTicks )
    print( 'ax.yaxis.minorTicks:', yax.minorTicks )

def fig_add_text():
    plt.figure()
    plt.text( 0.5, 0.5, 'Figure', ha='center',
              va='top', size=20, alpha=.5 )
    plt.xticks([]), plt.yticks([])
    plt.show()
    plt.text( 0.5, 0.5, 'Figure', ha='center',
              va='center', size=20, alpha=.5 )
    plt.xticks([]), plt.yticks([])
    plt.show()

def fig_add_pic():
    plt.figure()
    plt.xticks([]), plt.yticks([])
    im = np.array(Image.open('Houston Rockets.png'))
    plt.imshow(im)
    plt.show()

def fig_add_line():
    plt.figure()
    plt.plot([0, 1], [0, 1])
    plt.show()

def fig_add_subplot():
    plt.figure()
    plt.subplot(2,1,1)
    plt.xticks([]), plt.xticks([])
    plt.text(0.5, 0.5, 'subplot(2,1,1)', va='center', ha='center', size=10, alpha=.5)
    plt.subplot(2,1,2)
    plt.xticks([]), plt.xticks([])
    plt.text(0.5, 0.5, 'subplot(2,1,2)', va='center', ha='center', size=10, alpha=.5)
    plt.show()

def fig_add_multiplot():
    fig, axes = plt.subplots(nrows=2, ncols=2)
    for i, ax in enumerate(axes.flat):
        ax.set(xticks=[], yticks=[])
        s = 'subplot(2,2' + str(i) + ')'
        ax.text(0.5, 0.5, s, ha='center', va='center', size=20, alpha=0.5)
    plt.show()

def fig_add_grid():
    G = gridsec.GridSpec(3,3)
    ax1 = plt.subplot(G[0, :])
    plt.xticks([]), plt.yticks([])
    plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=20, alpha=0.5)

    ax2 = plt.subplot(G[1, :-1])
    plt.xticks([]), plt.yticks([])
    plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=20, alpha=0.5)

    ax3 = plt.subplot(G[1:, -1])
    plt.xticks([]), plt.yticks([])
    plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=20, alpha=0.5)
    plt.show()

def fig_add_tick():
    fig, ax = plt.subplots()
    ax.set_xlabel('label on x-axis')
    ax.set_ylabel('label on y-axis')

    for label in ax.xaxis.get_ticklabels():
        label.set_color(dt_hex)
        label.set_rotation(45)
        label.set_fontsize(20)

    for line in ax.yaxis.get_ticklines():
        line.set_color(dt_hex)
        line.set_markersize(500)
        line.set_markeredgewidth(30)

    print( ax.xaxis.get_label() )
    print( ax.xaxis.get_ticklocs() )
    print( ax.xaxis.get_ticklabels() )
    print( ax.xaxis.get_ticklines() )
    print( ax.xaxis.get_ticks_position() )
    print( ax.xaxis.get_major_ticks() )

    plt.show()

def fig_diff_ticker():
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 4))
    axes[0, 0].set_title('Original')

    axes[0, 1].spines['right'].set_color('none')
    axes[0, 1].spines['left'].set_color('none')
    axes[0, 1].spines['top'].set_color('none')
    axes[0, 1].set_title('Handle Spines')

    axes[0, 2].yaxis.set_major_locator(ticker.NullLocator())
    axes[0, 2].xaxis.set_ticks_position('bottom')
    axes[0, 2].set_title('Handle ticker label')

    axes[1, 0].tick_params(which='major', width=2.00)
    axes[1, 0].tick_params(which='major', length=10)
    axes[1, 0].tick_params(which='minor', width=.075)
    axes[1, 0].tick_params(which='minor', length=2.5)
    axes[1, 0].set_title('Handle Tick width/')

    axes[1, 1].set_xlim(0, 5)
    axes[1, 1].set_ylim(0, 1)
    axes[1, 1].set_title('handle Axis Limit')

    axes[1, 2].patch.set_color('black')
    axes[1, 2].patch.set_alpha(0.3)
    axes[1, 2].set_title('Handler Patch Color')
    plt.show()

def sp_perf_show():
    perf = pd.read_csv("sp500.csv", index_col=0, parse_dates=True, dayfirst=True)
    print(perf.head())

    #select part
    # spx = perf[['Adj Close']].loc['2007-01-01':'2010-01-01']
    spx = perf[['Adj Close']].loc['2007-01-03':'2007-01-03',]
    print(spx.head())
    print(type(spx))
    spx = perf[['Adj Close']].loc['2007-01-03':'2007-12-28',]
    print(spx.head())
    print(type(spx))
    plt.plot(spx.values)
    plt.show()


def sp_perf_show_detail():
    dt_hex = '#2b4750'
    perf = pd.read_csv("sp500.csv", index_col=0, parse_dates=True, dayfirst=True)
    spx = perf[['Adj Close']].loc['2007-01-03':'2009-12-28',]
    plt.figure(figsize=(8,4), dpi=100)
    plt.plot(spx.values, color='blue', linewidth=1.5, linestyle='-')

    #set x\y ticks
    plt.xticks(np.linspace(-100,800,10))

    plt.yticks(np.linspace(600,1800, 7))

    plt.xlim(-37.75, 780)
    plt.ylim(650, 1700)

    plt.show()

    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(spx.values, color=dt_hex, linewidth=2, linestyle='-')
    plt.show()

def sp_perf_ax_lim():
    dt_hex = '#2b4750'
    perf = pd.read_csv("sp500.csv", index_col=0, parse_dates=True, dayfirst=True)
    spx = perf[['Adj Close']].loc['2007-01-03':'2009-12-28',]

    fig = plt.figure(figsize=(10, 6), dpi=100)
    ax = fig.add_subplot(1, 1, 1)
    x = spx.index
    y = spx.values

    ax.plot(x, y, color='r', linewidth=2, linestyle='-')
    ax.set_xlim(['1/1/2007','1/1/2010'])
    ax.set_ylim(y.min() * 0.8, y.max() * 1.2)
    plt.show()


def

if __name__ == '__main__':
    # showfig()
    # fig_add_text()
    # fig_add_pic()
    # fig_add_line()
    # fig_add_subplot()
    # fig_add_multiplot()
    # fig_add_grid()
    # fig_add_tick()
    # fig_diff_ticker()
    # sp_perf_show()
    # sp_perf_show_detail()
    # sp_perf_ax_lim()

