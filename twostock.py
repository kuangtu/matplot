# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# x = np.arange(0., np.e, 0.01)
# y1 = np.exp(-x)
# y2 = np.log(x)
#
# fig = plt.figure()
#
# ax1 = fig.add_subplot(111)
# ax1.plot(x, y1)
# ax1.set_ylabel('Y values for exp(-x)')
# ax1.set_title("Double Y axis")
#
# ax2 = ax1.twinx()  # this is the important function
# ax2.plot(x, y2, 'r')
# ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Y values for ln(x)')
# ax2.set_xlabel('Same X for both exp(-x) and ln(x)')
#
# plt.show()

def readCSV1(filename1, filename2):
    df1 = pd.read_csv(filename1, sep=',')
    x = df1['time']
    y1 = df1['price']
    df2 = pd.read_csv(filename2, sep=",")
    y2 = df2['price']
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1)
    ax2 = ax1.twinx()
    ax2.plot(x, y2, 'r')
    plt.show()

def readTmp(filename):
    df2 = pd.read_csv(filename, sep=",")
    y2 = df2['price']
    print y2


if __name__ == '__main__':
    file1 = "hklv15.csv"
    file2 = "H30332.csv"
    readCSV1(file1, file2)
    # readTmp(file2)

