from simulators.constants_and_packages import *
from simulators.functions import *


class MetaAlgorithm(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def send_message(self, from_node, to_node):
        pass

    @abc.abstractmethod
    def move(self, node):
        pass

    @abc.abstractmethod
    def init_nodes_before_big_loops(self, graph, robots, targets):
        pass

    @abc.abstractmethod
    def init_nodes_before_small_loops(self, graph, robots, targets):
        pass

    @abc.abstractmethod
    def send_messages(self, iteration, graph, robots, targets):
        pass





