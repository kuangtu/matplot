__author__ = 'user'

import numpy as np
import matplotlib.pyplot as plt


def TextDemo():
    fig = plt.figure()
    fig.suptitle('fig sup title', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(1, 1, 1)
    # fig.subplots_adjust(top = 0.85)
    ax.set_title("axes title")
    ax.set_xlabel("xlable")
    ax.set_ylabel("ylable")
    ax.axis([0, 10, 0, 10])
    ax.text(1, 1, "test")
    plt.show()


def FigureDemo():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    fig.suptitle('figure title demo', fontsize=14, fontweight='bold')
    # plt.plot([1,2,3,4])
    ticker = np.arange(5)
    add = 0.5
    plt.plot([1, 2, 3, 4], [2, 3, 4, 5])
    ax.set_title("axes title")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    plt.xlim(1, 4)
    plt.ylim(1, 10)
    ax.set_xticks(ticker + 0.5)
    ax.set_xticklabels(['20150101','20150102','20150103','20150104'],rotation=45)

    # plt.getp(fig)
    plt.show()


def HistData():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N = 5
    menMeans = [18, 35, 30, 35, 27]
    menStd = [2, 3, 4, 1, 2]
    womenMeans = [25, 32, 34, 20, 25]
    womenStd = [3, 5, 2, 3, 3]

    # # necessary variables
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars

    ## the bars
    rects1 = ax.bar(ind, menMeans, width,
                    color='black',
                    yerr=menStd,
                    error_kw=dict(elinewidth=2, ecolor='red'))

    rects2 = ax.bar(ind + width, womenMeans, width,
                    color='red',
                    yerr=womenStd,
                    error_kw=dict(elinewidth=2, ecolor='black'))

    # axes and labels
    ax.set_xlim(-width, len(ind) + width)
    ax.set_ylim(0, 45)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    xTickMarks = ['Group' + str(i) for i in range(1, 6)]
    ax.set_xticks(ind + width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)

    ## add a legend
    ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
    plt.show()

if __name__ == '__main__':
    # TextDemo()
    FigureDemo()
    # HistData()