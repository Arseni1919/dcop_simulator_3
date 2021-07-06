from simulators.constants_and_packages import *
from simulators.algorithms.CAMS import *
from simulators.algorithms.random_walk import *
from simulators.algorithms.MetaAlgorithm import *
from simulators.algorithms.Max_sum_MST import Max_sum_MST
dictionary_of_algorithms = {
    RandomWalk.name: RandomWalk,
    # 'Max-sum_MST': Max_sum_MST_alg,
    CAMS.name: CAMS,
    Max_sum_MST.name: Max_sum_MST,
    # 'DSA_MST': DSA_MST,
}


def get_the_algorithm_object(name, params):
    return dictionary_of_algorithms[params['class']](name, params)
