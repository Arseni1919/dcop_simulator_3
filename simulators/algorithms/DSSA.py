import random
import time

from simulators.algorithms.DSA_MST import *


class DSSA(DSA_MST):
    name = 'DSSA'

    def __init__(self, name, params=None):
        super(DSSA, self).__init__(name, params)

    def init_message_boxes(self, all_agents):
        # init_message_boxes(all_agents, iterations=2)
        pass

    def move(self, graph, robots, targets):
        robot_to_robot_pos_list = {robot.name: [pos_name for pos_name in robot.domain] for robot in robots}
        new_robot_to_robot_pos_list, end_run = self.dssa_check(robots, robot_to_robot_pos_list)
        while not end_run:
            for node in robots:
                robot_pos_name_set = new_robot_to_robot_pos_list[node.name]
                next_pos_node = self.get_robot_pos_dsa_mst(node, graph, robots, targets, robot_pos_name_set)
                node.next_pos_node = next_pos_node
                if not next_pos_node:
                    raise ValueError('[ERROR]: no next_pos_node')
            new_robot_to_robot_pos_list, end_run = self.dssa_check(robots, robot_to_robot_pos_list)
        if count_future_collisions(robots) > 0:
            print(f'collisions: {count_collisions(robots)} \nfuture collisions: {count_future_collisions(robots)}')
            raise ValueError('[ERROR]: future collisions of robots > 0')
        # self.breakdowns_correction(robots)
        self.make_step(robots)

    def make_step(self, robots):
        for node in robots:
            node.prev_pos_node = node.pos_node
            node.pos_node = node.next_pos_node

    def breakdowns_correction(self, robots):
        breakdowns_correction(robots, self.params)

    def dssa_check(self, robots, robot_to_robot_pos_list):
        # robot_to_robot_pos_list = {robot.name: [pos_name for pos_name in robot.domain] for robot in robots}
        for robot in robots:
            for robot_nei in robot.neighbours:
                if robot.next_pos_node is None or robot_nei.next_pos_node is None:
                    continue
                if robot.next_pos_node is robot_nei.next_pos_node:
                    if robot.num > robot_nei.num:
                        if robot.next_pos_node is robot.pos_node:
                            robot_to_robot_pos_list[robot_nei.name].remove(robot.next_pos_node.name)
                            robot_nei.next_pos_node = None
                        else:
                            robot_to_robot_pos_list[robot.name].remove(robot.next_pos_node.name)
                            robot.next_pos_node = None
        end_run = not any([not node.next_pos_node for node in robots])
        return robot_to_robot_pos_list, end_run













