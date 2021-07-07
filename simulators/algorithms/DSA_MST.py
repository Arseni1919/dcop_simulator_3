import random
import time

from simulators.algorithms.MetaAlgorithm import *

class DSA_MST(MetaAlgorithm):
    name = 'DSA_MST'

    def __init__(self, name, params=None):
        super(DSA_MST, self).__init__(name, params)

    def send_message(self, from_node, to_node):
        raise RuntimeError

    def init_nodes_before_big_loops(self, graph, robots, targets):
        def init_message_box(x):
            x.message_box = {i: {} for i in range(B_ITERATIONS_IN_BIG_LOOPS)}
        list(map(init_message_box, robots))

    def init_nodes_before_small_loops(self, graph, robots, targets):
        # update robots domains
        _ = [robot.update_domain() for robot in robots]

        # update targets cells_near_me
        _ = [target.update_cells_near_me(robots, graph) for target in targets]

        # clean neighbours
        _ = [agent.clean_neighbours() for agent in [*graph, *robots, *targets]]

        self.set_neighbours(robots)

        # init message boxes
        init_message_boxes([*graph, *robots, *targets], iterations=2)

    def set_neighbours(self, robots):
        for robot1 in robots:
            for robot2 in robots:
                intersections = [pos1 in robot2.domain for pos1 in robot1.domain]
                if any(intersections):
                    robot1.neighbours.append(robot2)

    def send_messages(self, iteration, graph, robots, targets, problem, alg_num, tracker):
        pass

    def move(self, graph, robots, targets):
        for node in robots:
            next_pos_node = self.get_robot_pos_dsa_mst(node, graph, robots, targets)
            node.prev_pos_node = node.pos_node
            node.pos_node = next_pos_node

        self.breakdowns_correction(robots)

    def breakdowns_correction(self, robots):
        breakdowns_correction(robots, self.params)

    def get_robot_pos_dsa_mst(self, robot, graph, robots, targets):
        """
        1. temp_req_set
        2. select_pos
        3. if dsa_condition

        SELECT_POS ( select_pos(pos_set, targets, SR) ):
            input:
            pos_set = [(x1, y1),(x2, y2),..]
            targets = [(target, temp_req), (target, temp_req), ..]
            SR = int()
            output:
            pos = (x, y)
        """
        new_pos_node = select_pos(robot, targets, graph)
        if self.dsa_condition(robot, new_pos_node, robot.pos_node.pos, targets):
            return new_pos_node
        return robot.pos_node

    def calculate_temp_req(self, targets, neighbours):
        """
        input:
        output: [(target, temp_req), (), ...]
        """
        temp_req_set = []
        for target in targets:
            curr_tuple = (target, target.req)
            for nei in neighbours:
                if distance(nei.pos_node.pos, target.pos_node.pos) < nei.sr:
                    curr_tuple = (target, max(0, curr_tuple[1] - nei.cred))
            temp_req_set.append(curr_tuple)
        return temp_req_set

    def dsa_condition(self, agent, new_pos_node, curr_pos, targets):
        """
        input:
        output:
        More specifically, in DSA, the replacement
        decision takes into account whether a replacement of assignment will improve the
        local state of the agent. If so, a change is made with probability defined by parameter
        p. Zhang et al. showed that the value of p has a major effect on the quality of solutions
        found by DSA [63].
        """
        temp_req_set = self.calculate_temp_req(targets, agent.neighbours)
        curr_value = 0
        new_value = 0
        for (target, temp_req) in temp_req_set:
            if distance(new_pos_node.pos, target.pos_node.pos) < agent.sr:
                new_value += min(agent.cred, temp_req)
            if distance(curr_pos, target.pos_node.pos) < agent.sr:
                new_value += min(agent.cred, temp_req)
        if new_value >= curr_value:
            return random.random() < 0.7
        return False









