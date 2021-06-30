from constants_and_packages import *


def flatten_message(message):
    min_value = min(message.values())
    return {pos_i: value-min_value for pos_i, value in message.items()}










