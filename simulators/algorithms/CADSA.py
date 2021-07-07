import random
import time

from simulators.algorithms.DSA_MST import *


class CADSA(DSA_MST):
    name = 'CADSA'

    def __init__(self, name, params=None):
        super(CADSA, self).__init__(name, params)

    def move(self, graph, robots, targets):
        for node in robots:
            next_pos_node = self.get_robot_pos_dsa_mst(node, graph, robots, targets)
            node.next_pos_node = next_pos_node

        self.cadsa_correction(robots)
        self.breakdowns_correction(robots)

    def breakdowns_correction(self, robots):
        breakdowns_correction(robots, self.params)

    def cadsa_correction(self, robots):
        for robot in robots:
            for robot_nei in robot.neighbours:
                if robot.pos_node is robot_nei.pos_node:
                    if robot.num > robot_nei.num:
                        robot.next_pos_node = None
                        break
        for node in robots:
            node.prev_pos_node = node.pos_node
            if node.next_pos_node:
                node.pos_node = node.next_pos_node













