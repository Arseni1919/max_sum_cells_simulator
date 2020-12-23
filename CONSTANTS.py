import pygame
import sys
import os
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
import collections
from collections import namedtuple
import operator
from prettytable import PrettyTable
from termcolor import colored
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
OBJECTS = {}
# Define constants for the screen width and height
# SCREEN_WIDTH = 1000
SCREEN_WIDTH = 692
SCREEN_HEIGHT = 690
# SCREEN_WIDTH = SCREEN_HEIGHT + 202
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
# for logging
_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=_format, level=logging.INFO,
                    datefmt="%H:%M:%S")
# logging.getLogger().setLevel(logging.DEBUG)
ADDING_TO_FILE_NAME = ''

GRID_SIDE_SIZE = 50
NUM_OF_AGENTS = 80
NUM_OF_TARGETS = 20
NUMBER_OF_PROBLEMS = 10
ITERATIONS_IN_BIG_LOOPS = 20
ITERATIONS_IN_SMALL_LOOPS = 10
DELAY_OF_COLLISION = 18
EXECUTE_DELAY = True
# EXECUTE_DELAY = False
# TARGETS_APART = True
TARGETS_APART = False
ADDING_TO_FILE_NAME += '_targets_apart_' if TARGETS_APART else ''
ADDING_TO_FILE_NAME += '_delay_%s_' % DELAY_OF_COLLISION if EXECUTE_DELAY else ''

ALGORITHMS_TO_CHECK = [
    ('random_walk', {}),
    ('harels_algorithm', {}),
    ('max_sum_cells', {}),
]

CELL_SIZE['CUSTOM'] = int(SCREEN_HEIGHT / GRID_SIDE_SIZE - 2)
cell_size = CELL_SIZE['CUSTOM']
PADDING = 2
DISTANCE_BETWEEN_CELLS = cell_size + PADDING
# ---

alpha = 0.025  # for confidence intervals in graphs
speed = 5  # bigger - slower, smaller - faster. don't ask why
use_rate = False  # if False - it uses the num_of_targets variable, but still also uses target_rate
target_rate = 0.055
MINUS_INF = -50000
from_c_to_r = (2, 1)
# FLATTEN = False
FLATTEN = True

REQ = 120
MR = 2.5 * cell_size
SR = 2.5 * cell_size
CRED = 30

# -------------------------------------------------- #
# SHOW_RANGES = True
SHOW_RANGES = False
# NEED_TO_SAVE_RESULTS = False
NEED_TO_SAVE_RESULTS = True
NEED_TO_PLOT_RESULTS = True
NEED_TO_PLOT_VARIANCE = False
NEED_TO_PLOT_MIN_MAX = True
# -------------------------------------------------- #
FILE_NAME = "last_weights.txt"
# LOAD_PREVIOUS_POSITIONS = True
LOAD_PREVIOUS_POSITIONS = False
# LOAD_PREVIOUS_WEIGHTS = True
LOAD_PREVIOUS_WEIGHTS = False
SAVE_WEIGHTS = True
# SAVE_WEIGHTS = False




