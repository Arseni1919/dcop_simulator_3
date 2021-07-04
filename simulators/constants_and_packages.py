import abc
import itertools
import operator
import collections
from prettytable import PrettyTable
from termcolor import colored
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import pickle
import time
from pprint import pprint
from sklearn.neighbors import NearestNeighbors

S_ITERATIONS = 20
S_FLATTEN = True
MINUS_INF = -70000

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# For Big Simulations:
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

B_WIDTH = 50
B_HEIGHT = B_WIDTH
B_N_NODES = 500
B_MAX_DISTANCE_OF_NEARBY_POS = B_WIDTH/2
B_SIZE_ROBOT_NODE = B_WIDTH/50
B_SIZE_TARGET_NODE = B_WIDTH/50
B_MIN_NEARBY_POS = 4
B_MAX_NEARBY_POS = 7
B_ITERATIONS_IN_BIG_LOOPS = 100
B_ITERATIONS_IN_SMALL_LOOPS = 30
# B_ITERATIONS_IN_BIG_LOOPS = 20
B_NUMBER_OF_PROBLEMS = 50
# B_NUMBER_OF_PROBLEMS = 2
B_NUM_OF_ROBOTS = 8
# B_NUM_OF_ROBOTS = 1
B_NUM_OF_TARGETS = 2

GRID_SIDE_SIZE = 50
# GRID_SIDE_SIZE = 20
DELAY_OF_COLLISION = 100
# EXECUTE_DELAY = True
EXECUTE_DELAY = False
# TARGETS_APART = True
TARGETS_APART = False

ADDING_TO_FILE_NAME = ''
ADDING_TO_FILE_NAME += '%sT-%sR_' % (B_NUM_OF_TARGETS, B_NUM_OF_ROBOTS)
ADDING_TO_FILE_NAME += '%sBi-%sSi_' % (B_ITERATIONS_IN_BIG_LOOPS, B_ITERATIONS_IN_SMALL_LOOPS)
ADDING_TO_FILE_NAME += '%sPRBLMS_' % (B_NUMBER_OF_PROBLEMS,)
ADDING_TO_FILE_NAME += 'targets_apart_' if TARGETS_APART else ''
ADDING_TO_FILE_NAME += 'delay-v2_%s' % DELAY_OF_COLLISION if EXECUTE_DELAY else ''

ALGORITHMS_TO_CHECK = [
    ('Random-Walk', {}),
    # ('Max-sum_MST', {}),
    # ('CAMS', {}),
    # ('DSA_MST', {}),
]

# -------------------------------------------------- #
SHOW_RANGES = True
# SHOW_RANGES = False
SAVE_RESULTS = True
# SAVE_RESULTS = False
NEED_TO_PLOT_RESULTS = True
# NEED_TO_PLOT_VARIANCE, NEED_TO_PLOT_MIN_MAX = False, True
NEED_TO_PLOT_VARIANCE, NEED_TO_PLOT_MIN_MAX = True, False
LIGHT_UP_THE_CHANGES = True
# LIGHT_UP_THE_CHANGES = False
AMOUNT_OF_STD = 1
# -------------------------------------------------- #
FILE_NAME = "last_weights.txt"
# LOAD_PREVIOUS_POSITIONS = True
LOAD_PREVIOUS_POSITIONS = False
# LOAD_PREVIOUS_WEIGHTS = True
LOAD_PREVIOUS_WEIGHTS = False
SAVE_WEIGHTS = True
# SAVE_WEIGHTS = False

