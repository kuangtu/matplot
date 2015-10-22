__author__ = 'user'

import numpy as np
from pylab import *

def plotdemo():
    X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
    C,S = np.cos(X),np.sin(X)
    subplot(1,2,1)
    plot(X,C)
    plot(X,S)

    subplot(1,2,2)
    plot(X,C)
    plot(X,S)
    show()


def 



if __name__ == '__main__':
    plotdemo()