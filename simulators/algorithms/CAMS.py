from simulators.algorithms.MetaAlgorithm import *


class CAMS(MetaAlgorithm):
    def __init__(self, name):
        super(CAMS, self).__init__(name)
        pass

    def send_message(self, from_node, to_node):
        pass

    def move(self, node):
        pass

    def init_nodes_before_big_loops(self, graph, robots, targets):
        # super(CAMS, self).init_nodes_before_big_loops(graph, robots, targets)
        pass

    def init_nodes_before_small_loops(self, graph, robots, targets):
        pass

CAMS_alg = CAMS('CAMS')
