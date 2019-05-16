import matplotlib as mpl
import matplotlib.gridspec as gridsec
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


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
    plt.x
    plt.show()

if __name__ == '__main__':
    # showfig()
    # fig_add_text()
    # fig_add_pic()
    # fig_add_line()
    # fig_add_subplot()
    # fig_add_multiplot()
    fig_add_grid()

