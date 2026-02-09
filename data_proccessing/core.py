
def pressure_to_height(pressure):
    """
    source: https://github.com/TheAlgorithms/Python/blob/master/physics/altitude_pressure.py
    :param pressure: in pascals
    :return: height in
    """
    return 44_330 * (1 - (pressure / 101_325) ** (1 / 5.5255))


def remove_outliers(data, m=2,axis=None):
    """

    :param data: a array of [x,y] value pairs
    :param axis: the axis to identify outliers by
    :return:
    """
    # todo: is all data usefull? if so, then implement

