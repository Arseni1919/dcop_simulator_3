from simulators.constants_and_packages import *


class MetaAlgorithm(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def send_message(self, from_node, to_node):
        pass

    @abc.abstractmethod
    def move(self, node):
        pass






