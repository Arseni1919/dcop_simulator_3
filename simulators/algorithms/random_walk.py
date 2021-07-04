import random
import time

from simulators.algorithms.MetaAlgorithm import *



class RandomWalk(MetaAlgorithm):

    def __init__(self, name):
        super(RandomWalk, self).__init__(name)
        pass

    def send_message(self, from_node, to_node):
        pass

    def move(self, node):
        if 'robot' in node.name:
            possible_next_positions = list(node.pos_node.nearby_position_nodes.values())
            possible_next_positions.append(node.pos_node)
            # print(f'in: {node.pos_node.num}, to move: {[n.num for n in possible_next_positions]}')
            next_position = random.sample(possible_next_positions, 1)[0]
            node.prev_pos_node = node.pos_node
            node.pos_node = next_position
            # time.sleep(1)

    def init_nodes_before_big_loops(self, graph, robots, targets):
        list(map(init_message_box, robots))

    def init_nodes_before_small_loops(self, graph, robots, targets):
        list(map(update_domain, robots))

    def send_messages(self, iteration, graph, robots, targets):
        pass


random_walk = RandomWalk('Random-Walk')


