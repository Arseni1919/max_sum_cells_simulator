from CONSTANTS import *
from max_sum_cells import *

dictionary_of_algorithms = {
    'max_sum_cells': max_sum_cells_alg,
}


def get_the_algorithm(name):
    return dictionary_of_algorithms[name]
