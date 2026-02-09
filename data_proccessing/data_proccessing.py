import numpy as np

def slice_data(data,index,axis):
    """
    Splits the data into multiple sections.
    :param data: data to be sliced
    :param index: either a int or a list of ints, [2,3] results in :2, 2:3 and 3:
    :param axis: the axis to be sliced
    :return: array of slices
    """
    return np.split(data,index,axis)

def pressure_to_height(pressure):
    """
    source: https://github.com/TheAlgorithms/Python/blob/master/physics/altitude_pressure.py
    :param pressure: in pascals
    :return: height in
    """
    return 44_330 * (1 - (pressure / 101_325) ** (1 / 5.5255))


def remove_outliers(data, m=2,axis=None):
    """
    :param data: an array of [x,y] value pairs
    :param m: number of standard deviations the data can be from the mean
    :param axis: the axis to identify outliers by
    :return:
    """
    # todo: is all data useful? if so, then implement

