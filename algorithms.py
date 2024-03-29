from CONSTANTS import *
from CAMS import *
from DSA_MST import DSA_MST
from random_walk import random_walk
from Max_sum_MST import Max_sum_MST_alg

dictionary_of_algorithms = {
    'Random-Walk': random_walk,
    'Max-sum_MST': Max_sum_MST_alg,
    'CAMS': CAMS_alg,
    'DSA_MST': DSA_MST,
}


def get_the_algorithm(name):
    return dictionary_of_algorithms[name]
