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
from pprint import pprint
from sklearn.neighbors import NearestNeighbors

S_ITERATIONS = 20
S_FLATTEN = True
MINUS_INF = -70000

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

B_WIDTH = 500
B_HEIGHT = B_WIDTH

B_N_NODES = 500

B_MAX_DISTANCE_OF_NEARBY_POS = 50


