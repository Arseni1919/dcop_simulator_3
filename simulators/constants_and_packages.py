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
import os
from scipy.stats import ttest_ind

S_ITERATIONS = 20
MINUS_INF = -70000
FLATTEN_MESSAGE = True
# FLATTEN_MESSAGE = False

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# For Big Simulations:
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

B_WIDTH = 100
B_HEIGHT = B_WIDTH
B_MAX_DISTANCE_OF_NEARBY_POS = B_WIDTH / 3
B_SIZE_ROBOT_NODE = B_WIDTH / 50
B_SIZE_TARGET_NODE = B_WIDTH / 50
B_MIN_NEARBY_POS = 3
B_MAX_NEARBY_POS = 5


# B_ITERATIONS_IN_BIG_LOOPS = 100
B_ITERATIONS_IN_BIG_LOOPS = 1
# B_ITERATIONS_IN_SMALL_LOOPS = 30
B_ITERATIONS_IN_SMALL_LOOPS = 1

# B_NUMBER_OF_PROBLEMS = 50
B_NUMBER_OF_PROBLEMS = 1
B_N_NODES = 100
B_NUM_OF_ROBOTS = 10
# B_NUM_OF_ROBOTS = 1
B_NUM_OF_TARGETS = 7


MR = B_MAX_DISTANCE_OF_NEARBY_POS/2.5
SR = MR

GRID_SIDE_SIZE = 50
# GRID_SIDE_SIZE = 20
DELAY_OF_COLLISION = 100
# EXECUTE_DELAY = True
EXECUTE_DELAY = False
# TARGETS_APART = True
TARGETS_APART = False
DIFF_CRED = True
# DIFF_CRED = False
MIN_CRED, MAX_CRED = 10, 40

ADDING_TO_FILE_NAME = ''
ADDING_TO_FILE_NAME += '%sT-%sR_' % (B_NUM_OF_TARGETS, B_NUM_OF_ROBOTS)
ADDING_TO_FILE_NAME += '%sBi-%sSi_' % (B_ITERATIONS_IN_BIG_LOOPS, B_ITERATIONS_IN_SMALL_LOOPS)
ADDING_TO_FILE_NAME += '%sPRBLMS_' % (B_NUMBER_OF_PROBLEMS,)
ADDING_TO_FILE_NAME += 'targets_apart_' if TARGETS_APART else ''
ADDING_TO_FILE_NAME += 'delay-v2_%s' % DELAY_OF_COLLISION if EXECUTE_DELAY else ''

ALGORITHMS_TO_CHECK = [
    # ('CAMS_diff_creds', {
    #     'class': 'CAMS',
    #     'diff_creds': {
    #         'min': 5,
    #         'max': 30,
    #     },
    # }),
    ('CAMS_breakdowns', {
        'class': 'CAMS',
        'breakdowns': True,
    }),
    ('CAMS', {
        'class': 'CAMS'
    }),
    ('CADSA', {
        'class': 'CADSA',
    }),
    ('Max-sum_MST_breakdowns', {
        'class': 'Max_sum_MST',
        'breakdowns': True,
    }),
    ('DSA_MST_breakdowns', {
        'class': 'DSA_MST',
        'breakdowns': True,
    }),
    ('DSA_MST', {
        'class': 'DSA_MST',
    }),
    ('Max_sum_MST', {
        'class': 'Max_sum_MST',
    }),
    # ('Random-Walk', {
    #     'class': 'RandomWalk'
    # }),
    # ('Random-Walk_breakdowns', {
    #     'class': 'RandomWalk',
    #     'breakdowns': True,
    # }),

]

# -------------------------------------------------- #
NEED_TO_PLOT_FIELD = True
# NEED_TO_PLOT_FIELD = False
SHOW_RANGES = True
# SHOW_RANGES = False
PICKLE_RESULTS = True
# PICKLE_RESULTS = False
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
