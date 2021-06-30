import abc

from functions import *


class Node(abc.ABC):
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.neighbours = []
        # iteration -> name -> position -> value
        self.message_box = {}

        if str(num) not in name:
            raise RuntimeError('num is not in name')

    @abc.abstractmethod
    def send_message_to(self, nei, iteration):
        pass


class TargetNode(Node):
    def __init__(self, name, num, req: int):
        super().__init__(name, num)
        self.req = req

        if 'target' not in name:
            raise RuntimeError('target is not in name')

    def send_message_to(self, nei, iteration):
        message = {pos_i: -9999999 for pos_i in nei.domain}


class PositionNode(Node):
    def __init__(self, name, num, dict_of_weights: dict):
        super().__init__(name, num)
        self.dict_of_weights = dict_of_weights

        if 'pos' not in name:
            raise RuntimeError('pos is not in name')

    def send_message_to(self, nei, iteration):
        message = {pos_i: -9999999 for pos_i in nei.domain}


class RobotNode(Node):
    def __init__(self, name, num, cred: int, domain: list):
        super().__init__(name, num)
        self.cred = cred
        self.domain = domain

        if 'robot' not in name:
            raise RuntimeError('robot is not in name')

    def send_message_to(self, func_nei, iteration):
        message = {pos_i: 0 for pos_i in self.domain}

        if iteration > 0:
            for nei in self.neighbours:
                if nei.name != func_nei.name:
                    past_message = self.message_box[iteration - 1][nei.name]
                    for d in self.domain:
                        message[d] += past_message[d]
        if FLATTEN:
            message = flatten_message(message)
        func_nei.message_box[iteration][self.name] = message



