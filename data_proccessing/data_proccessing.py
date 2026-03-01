import random
import csv
import numpy as np
import math

# target: https://docs.google.com/document/d/1ZrHmUzFSbimNmvZLT4MfxJwNgPxCKA-LfHc2wqpyyek/edit?tab=t.0

def slice_data_by_time_example(array,min,max):
    b=array[(min<=array[:,1])&(array[:,1]<max)]

def slice_data_by_index(data,index,axis):
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

def barametric_formula(height,P_b, T, R_Star=8.31432*10**3, g=9.8, M=28.9644, H=0):
    """
    Calculates Pressure as a function of base pressure,
    height and temperature, assuming no temperature gradient.

    I hope this was copied from wikipedia correctly.
    :param P_b: base pressure
    :param height: height
    :param T: temperature
    :param R_Star: the universal gas constant
    :param g: the gravitational acceleration
    :param M: mean molar mass of air
    :param H: base height
    :return P: The expected pressure
    """
    P = P_b*math.exp(
        (-g*M*(height-H)) /
        (R_Star*T)
    )
    return P

def inverse_barametric_formula(P,P_b, T, R_Star=8.31432*10**3, g=9.8, M=28.9644, H=0):
    height=(R_Star*T)*math.log(P/P_b)/(-g*M)+H
    return height

def diferenciate(x_list, y_list):
    return np.diff(y_list)/np.diff(x_list)



def proces_radio(temperature,pressure,time):
    temperature=np.array(temperature)
    pressure=np.array(pressure)
    time=np.array(time)
    height = inverse_barametric_formula(pressure,pressure[0],temperature)
    speed_y = diferenciate(height,time)
    acceleration_y = diferenciate(speed_y,time)

def load_from_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return list(reader)

for i in range(1,10):
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(inverse_barametric_formula(barametric_formula(i,a,b),a,b))
if __name__ == "__main__":
    pass