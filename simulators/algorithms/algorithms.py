from simulators.constants_and_packages import *
from simulators.algorithms.CAMS import CAMS_alg
from simulators.algorithms.random_walk import random_walk
from simulators.algorithms.MetaAlgorithm import *

dictionary_of_algorithms = {
    random_walk.name: random_walk,
    # 'Max-sum_MST': Max_sum_MST_alg,
    CAMS_alg.name: CAMS_alg,
    # 'DSA_MST': DSA_MST,
}


def get_the_algorithm_object(name):
    return dictionary_of_algorithms[name]
