from numpy.polynomial.polynomial import polyfit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from data_proccessing.core import remove_outliers

def demmo_hist():
    before = np.random.randn(100, 3)
    plt.hist(pd.DataFrame(before))
    plt.show()
    plt.hist(remove_outliers(before))
    plt.show()


def plot_best_fit(data,show=True):
    """

    :param data: a array of x y values
    :return: None
    """
    x = data[:, 0]
    y = data[:, 1]
    b, m = polyfit(x, y, 1)
    plt.plot(x, b + m * x, '-')
    if show:
        plt.show()

def plot_points(data,show=True):
    """

    :param x:
    :param y:
    :param show:
    :return:
    """
    x = data[:, 0]
    y = data[:, 1]
    plt.plot(x, y, '.')
    if show:
        plt.show()

def plot_test():

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

def scatter_plot_data(data, radius=20.0,label="Data",colour="tab:blue",show=True):
    """

    >>> scatter_plot_data(np.random.randn(100, 2))

    :param data: the data to be plotted, a list of arrays [x,y]
    :param radius: the radius of each point on the scatter plot
    :param label: The label of the data
    :return: None
    """
    fig, ax = plt.subplots()
    n = 750
    x = data[:,0]
    y = data[:,1]

    #x, y = np.random.rand(2, n)
    scale = [radius for _ in data]# * np.random.rand(n)
    ax.scatter(x, y, c=colour, s=scale, label=label,
               alpha=0.3, edgecolors='none')
    if show:
        ax.legend()
        ax.grid(True)

        plt.show()
