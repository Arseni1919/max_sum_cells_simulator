import pygame
import sys
import random
import logging
import threading
import time
import concurrent.futures
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import numpy as np
import pickle
import json
import copy
from scipy.stats import t
from scipy import stats
import itertools
# from tqdm import tqdm
from pprint import pprint
import statistics
from collections import namedtuple

CellTuple = namedtuple('CellTuple', ['pos',])
TargetTuple = namedtuple('TargetTuple', ['pos', 'req', 'name', 'num'])
AgentTuple = namedtuple('AgentTuple', ['pos', 'num_of_robot_nei', 'num_of_target_nei', 'name', 'num', 'cred', 'SR', 'MR'])
MessageType = namedtuple('MessageType', ['from_var_to_func',
                                         'from_var_to_func_only_pos',
                                         'from_var_to_func_dir',
                                         'from_func_pos_collisions_to_var',
                                         'from_func_dir_collisions_to_var',
                                         'from_func_target_to_var'])
message_types = MessageType(from_var_to_func='from_var_to_func',
                            from_var_to_func_only_pos='from_var_to_func_only_pos',
                            from_var_to_func_dir='from_var_to_func_dir',
                            from_func_pos_collisions_to_var='from_func_pos_collisions_to_var',
                            from_func_dir_collisions_to_var='from_func_dir_collisions_to_var',
                            from_func_target_to_var='from_func_target_to_var')
from_func_to_var_types = (message_types.from_func_pos_collisions_to_var, message_types.from_func_target_to_var,
                          message_types.from_func_dir_collisions_to_var)
dictionary_message_types = (message_types.from_func_pos_collisions_to_var, message_types.from_func_target_to_var,
                            message_types.from_func_dir_collisions_to_var, message_types.from_var_to_func,
                            message_types.from_var_to_func_dir)
TypesOfRequirement = namedtuple('TypesOfRequirement', ['copy', 'copy_var_dicts', 'copy_func_dicts'])
copy_types = TypesOfRequirement('copy', 'copy_var_dicts', 'copy_func_dicts')


OBJECTS = {}


# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 690
# SCREEN_HEIGHT = 850

# have to be odd number for move method of Agent
CELL_SIZE = {
    'SMALL': 18,
    'MEDIUM': 34,
    'BIG': 74,
    'CUSTOM': 10,
}

SKY_COLOR = (135, 206, 250)
# SPEED_MOVING = 10

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# for logging
_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=_format, level=logging.INFO,
                    datefmt="%H:%M:%S")
# logging.getLogger().setLevel(logging.DEBUG)

GRID_SIDE_SIZE = 10
CELL_SIZE['CUSTOM'] = int(SCREEN_HEIGHT / GRID_SIDE_SIZE - 2)
cell_size = CELL_SIZE['CUSTOM']
# ---
show_ranges = True
need_to_save_results = False
adding_to_file_name = ''
need_to_plot_results = True
need_to_plot_variance = False
need_to_plot_min_max = True
alpha = 0.025  # for confidence intervals in graphs
speed = 5  # bigger -slower, smaller - faster. don't ask why
num_of_agents = 4
num_of_targets = 4
use_rate = False  # if False - it uses the num_of_targets variable, but still also uses target_rate
target_rate = 0.055

target_range = (100, 100)  # max and min value of target
MR = 2.5 * cell_size
SR = 2.5 * cell_size
cred = 30
ITERATIONS = 10
NUMBER_OF_PROBLEMS = 10

algorithms_to_check = [
    ('max_sum_cells', {}),
]
