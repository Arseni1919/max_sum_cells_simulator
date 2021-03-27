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
from scipy.stats import ttest_ind
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
OBJECTS_SPRITES = {}
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
# GRID_SIDE_SIZE = 20
NUM_OF_AGENTS = 80
NUM_OF_TARGETS = 20
NUMBER_OF_PROBLEMS = 50
# NUMBER_OF_PROBLEMS = 5
ITERATIONS_IN_BIG_LOOPS = 100
# ITERATIONS_IN_BIG_LOOPS = 10
ITERATIONS_IN_SMALL_LOOPS = 30
DELAY_OF_COLLISION = 100
EXECUTE_DELAY = True
# EXECUTE_DELAY = False
# TARGETS_APART = True
TARGETS_APART = False

ADDING_TO_FILE_NAME += '%sGrid-_' % (GRID_SIDE_SIZE,)
ADDING_TO_FILE_NAME += '%sT-%sR_' % (NUM_OF_TARGETS, NUM_OF_AGENTS)
ADDING_TO_FILE_NAME += '%sBi-%sSi_' % (ITERATIONS_IN_BIG_LOOPS, ITERATIONS_IN_SMALL_LOOPS)
ADDING_TO_FILE_NAME += '%sPRBLMS_' % (NUMBER_OF_PROBLEMS,)
ADDING_TO_FILE_NAME += 'col-v2_'
ADDING_TO_FILE_NAME += 'targets_apart_' if TARGETS_APART else ''
ADDING_TO_FILE_NAME += 'delay-v2_%s' % DELAY_OF_COLLISION if EXECUTE_DELAY else ''

ALGORITHMS_TO_CHECK = [
    # ('Random-Walk', {}),
    # ('Max-sum_MST', {}),
    # ('CAMS', {}),
    ('DSA_MST', {}),
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
MR = 1.5 * cell_size
SR = 1.5 * cell_size
CRED = 30

# -------------------------------------------------- #
SHOW_RANGES = True
# SHOW_RANGES = False
SAVE_RESULTS = True
# SAVE_RESULTS = False
NEED_TO_PLOT_RESULTS = True
# NEED_TO_PLOT_VARIANCE, NEED_TO_PLOT_MIN_MAX = False, True
NEED_TO_PLOT_VARIANCE, NEED_TO_PLOT_MIN_MAX = True, False
AMOUNT_OF_STD = 1
# -------------------------------------------------- #
FILE_NAME = "last_weights.txt"
# LOAD_PREVIOUS_POSITIONS = True
LOAD_PREVIOUS_POSITIONS = False
# LOAD_PREVIOUS_WEIGHTS = True
LOAD_PREVIOUS_WEIGHTS = False
SAVE_WEIGHTS = True
# SAVE_WEIGHTS = False




