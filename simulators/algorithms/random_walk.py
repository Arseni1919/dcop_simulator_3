import random
import time

from simulators.algorithms.MetaAlgorithm import *


class RandomWalk(MetaAlgorithm):
    name = 'RandomWalk'

    def __init__(self, name, params=None):
        super(RandomWalk, self).__init__(name, params)

    def send_message(self, from_node, to_node):
        raise RuntimeError

    def move(self, graph, robots, targets):
        for node in robots:
            possible_next_positions = list(node.pos_node.nearby_position_nodes.values())
            possible_next_positions.append(node.pos_node)
            # print(f'in: {node.pos_node.num}, to move: {[n.num for n in possible_next_positions]}')
            next_position = random.sample(possible_next_positions, 1)[0]
            node.prev_pos_node = node.pos_node
            node.pos_node = next_position
            # time.sleep(1)

    def init_nodes_before_big_loops(self, graph, robots, targets):
        def init_message_box(x):
            x.message_box = {i: {} for i in range(B_ITERATIONS_IN_BIG_LOOPS)}
        list(map(init_message_box, robots))

    def init_nodes_before_small_loops(self, graph, robots, targets):
        # update robots domains
        _ = [robot.update_domain() for robot in robots]

        # clean neighbours
        _ = [agent.clean_neighbours() for agent in [*graph, *robots, *targets]]

        self.set_neighbours(robots)

    def set_neighbours(self, robots):
        for robot1 in robots:
            for robot2 in robots:
                intersections = [pos1 in robot2.domain for pos1 in robot1.domain]
                if any(intersections):
                    robot1.neighbours.append(robot2)


    def send_messages(self, iteration, graph, robots, targets, problem, alg_num, tracker):
        pass

    def breakdowns_correction(self, robots):
        breakdowns_correction(robots, self.params)


random_walk = RandomWalk('Random-Walk')


