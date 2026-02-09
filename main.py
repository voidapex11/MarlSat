import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from numpy.polynomial.polynomial import polyfit

def plot_best_fit(x,y,plot=True):
    """

    :param x: a array of x axis values
    :param y: a array of y axis values
    :return: None
    """
    b, m = polyfit(x, y, 1)
    plt.plot(x, b + m * x, '-')
    if plot:
        plt.show()

def plot_points(x,y,show=True):
    """

    :param x:
    :param y:
    :param show:
    :return:
    """
    plt.plot(x, y, '.')
    if show:
        plt.show()

def plot_test():

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

def scatter_plot_data(data, radius=20.0,label="Data",show=True):
    """

    >>> scatter_plot_data(np.random.randn(100, 2))

    :param data: the data to be plotted, a list of arrays [x,y]
    :param radius: the radius of each point on the scatter plot
    :param label: The label of the data
    :return: None
    """
    fig, ax = plt.subplots()
    n = 750
    x = [data[i][0] for i in range(len(data))]
    y = [data[i][1] for i in range(len(data))]

    #x, y = np.random.rand(2, n)
    scale = [radius for _ in data]# * np.random.rand(n)
    ax.scatter(x, y, c="tab:blue", s=scale, label=label,
               alpha=0.3, edgecolors='none')
    if show:
        ax.legend()
        ax.grid(True)

        plt.show()

def remove_outliers(data):
    df = pd.DataFrame(data)

    return df[(np.abs(sp.stats.zscore(df)) < 3).all(axis=1)]

def hist():
    before = np.random.randn(100, 3)
    plt.hist(pd.DataFrame(before))
    plt.hist(remove_outliers(before))
    plt.show()


def main():
    x = np.arange(40)
    y = 5 * x + 10 + 20*np.random.randn(40)
    plot_points(x,y,show=False)
    plot_best_fit(x,y)


if __name__ == "__main__":
    main()
