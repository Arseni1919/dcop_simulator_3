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
import datetime

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
B_MAX_NEARBY_POS = 7
GRAPH_TYPE = 'complex'
# GRAPH_TYPE = 'grid'
GRID_SIZE_SIDE_WH = 25  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# GRID_SIZE_SIDE_WH = 4

B_ITERATIONS_IN_BIG_LOOPS = 20  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# B_ITERATIONS_IN_BIG_LOOPS = 10
B_ITERATIONS_IN_SMALL_LOOPS = 8  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# B_ITERATIONS_IN_SMALL_LOOPS = 2

B_NUMBER_OF_PROBLEMS = 50   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# B_NUMBER_OF_PROBLEMS = 1
B_N_NODES = 625  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
B_NUM_OF_ROBOTS = 30  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# B_NUM_OF_ROBOTS = 4
B_NUM_OF_TARGETS = 20  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# B_NUM_OF_TARGETS = 1

MR = B_MAX_DISTANCE_OF_NEARBY_POS/4.5  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MR = 30
SR = MR  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

GRID_SIDE_SIZE = 50
# GRID_SIDE_SIZE = 20
DELAY_OF_COLLISION = 100
# EXECUTE_DELAY = True
EXECUTE_DELAY = False
TARGETS_APART = True
# TARGETS_APART = False
REQ_OF_TARGETS = 300  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
DIFF_CRED = True
# DIFF_CRED = False
# MIN_CRED, MAX_CRED = 40, 45
MIN_CRED, MAX_CRED = 25, 50  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

ADDING_TO_FILE_NAME = ''
ADDING_TO_FILE_NAME += '%s_req_' % REQ_OF_TARGETS
ADDING_TO_FILE_NAME += '%sT-%sR_' % (B_NUM_OF_TARGETS, B_NUM_OF_ROBOTS)
ADDING_TO_FILE_NAME += '%sBi-%sSi_' % (B_ITERATIONS_IN_BIG_LOOPS, B_ITERATIONS_IN_SMALL_LOOPS)
ADDING_TO_FILE_NAME += '%sPRBLMS_' % (B_NUMBER_OF_PROBLEMS,)
ADDING_TO_FILE_NAME += 'targets_apart_' if TARGETS_APART else ''
ADDING_TO_FILE_NAME += 'delay-v2_%s' % DELAY_OF_COLLISION if EXECUTE_DELAY else ''
ADDING_TO_FILE_NAME += GRAPH_TYPE
ADDING_TO_FILE_NAME += f'_{B_MIN_NEARBY_POS}_{B_MAX_NEARBY_POS}' if GRAPH_TYPE == 'complex' else ''

ALGORITHMS_TO_CHECK = [
    # ('CAMS', {
    #     'class': 'CAMS',
    #     'breakdowns': True,
    #     'type': 'basic',
    # }),
    ('CAMS_delta', {
        'class': 'CAMS',
        'breakdowns': True,
        'type': 'delta',
    }),
    # ('CAMS_delta_from_single', {
    #     'class': 'CAMS',
    #     'breakdowns': True,
    #     'type': 'delta_from_single',
    # }),
    ('Max-sum_MST_breakdowns', {
        'class': 'Max_sum_MST',
        'breakdowns': True,
        'type': 'basic',
    }),
    # ('Max_sum_MST', {
    #     'class': 'Max_sum_MST',
    #     'type': 'basic',
    # }),
    ('Max_sum_MST_delta', {
        'class': 'Max_sum_MST',
        'type': 'delta',
    }),
    # ('Max_sum_MST_delta_from_single', {
    #     'class': 'Max_sum_MST',
    #     'type': 'delta_from_single',
    # }),
    ('DSSA', {
        'class': 'DSSA'
    }),
    ('DSA_MST', {
        'class': 'DSA_MST',
    }),
    ('CADSA', {
        'class': 'CADSA',
    }),
    ('Random-Walk', {
        'class': 'RandomWalk'
    }),


    # ('CAMS_diff_creds', {
    #     'class': 'CAMS',
    #     'diff_creds': {
    #         'min': 5,
    #         'max': 30,
    #     },
    # }),DSSA
    # ('CAMS_breakdowns', {
    #     'class': 'CAMS',
    #     'breakdowns': True,
    # }),
    # ('DSA_MST_breakdowns', {
    #     'class': 'DSA_MST',
    #     'breakdowns': True,
    # }),
    # ('Random-Walk_breakdowns', {
    #     'class': 'RandomWalk',
    #     'breakdowns': True,
    # }),

]

# -------------------------------------------------- #
# NEED_TO_PLOT_FIELD = True
NEED_TO_PLOT_FIELD = False
# NEED_TO_PRINT_DURATION = True
NEED_TO_PRINT_DURATION = False
# SHOW_RANGES = True
SHOW_RANGES = False
PICKLE_RESULTS = True
# PICKLE_RESULTS = False
LIGHT_UP_THE_CHANGES = True
# LIGHT_UP_THE_CHANGES = False
AMOUNT_OF_STD = 1
# -------------------------------------------------- #
FILE_NAME = "last_weights.txt"
# LOAD_PREVIOUS_POSITIONS = True
LOAD_PREVIOUS_POSITIONS = False
# LOAD_PREVIOUS_WEIGHTS = True
LOAD_PREVIOUS_WEIGHTS = False
# SAVE_WEIGHTS = True
# SAVE_WEIGHTS = False
