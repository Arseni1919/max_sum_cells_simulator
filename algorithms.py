from CONSTANTS import *
from max_sum_cells import *
from random_walk import random_walk
from  harels_algorithm import harels_algorithm

dictionary_of_algorithms = {
    'max_sum_cells': max_sum_cells_alg,
    'random_walk': random_walk,
    'harels_algorithm': harels_algorithm,
}


def get_the_algorithm(name):
    return dictionary_of_algorithms[name]
