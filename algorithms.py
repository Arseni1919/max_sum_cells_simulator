from CONSTANTS import *
from max_sum_cells import *
from random_walk import random_walk
from harels_algorithm import harels_algorithm

dictionary_of_algorithms = {
    'Random-Walk': random_walk,
    'Max-sum_MST': harels_algorithm,
    'CAMS': max_sum_cells_alg,
}


def get_the_algorithm(name):
    return dictionary_of_algorithms[name]
