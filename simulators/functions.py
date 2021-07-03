import random

from simulators.constants_and_packages import *


def flatten_message(message):
    if S_FLATTEN:
        min_value = min(message.values())
        return {pos_i: value-min_value for pos_i, value in message.items()}
    return message


def create_dict_of_weights(robots):
    # return_value = {robot.name: random.uniform(1e-3, 1e-1) for robot in robots}
    return_value = {robot.name: random.uniform(1e-10, 1e-5) for robot in robots}
    # return_value = {robot.name: 0 for robot in robots}
    return return_value












