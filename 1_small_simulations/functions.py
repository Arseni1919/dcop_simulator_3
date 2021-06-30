import random

from constants_and_packages import *


def flatten_message(message):
    if FLATTEN:
        min_value = min(message.values())
        return {pos_i: value-min_value for pos_i, value in message.items()}
    return message


def create_dict_of_weights(robots):
    return {robot.name: random.uniform(1e-5, 1e-2) for robot in robots}












