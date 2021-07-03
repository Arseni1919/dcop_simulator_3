from simulators.algorithms.MetaAlgorithm import *


class CAMS(MetaAlgorithm):
    def __init__(self, name):
        super(CAMS, self).__init__(name)
        pass

    def foo(self):
        pass

    def send_message(self, from_node, to_node):
        pass

    def move(self, node):
        pass


CAMS_alg = CAMS('CAMS')
