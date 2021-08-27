import random
import time

from simulators.algorithms.DSA_MST import *


class CADSA(DSA_MST):
    name = 'CADSA'

    def __init__(self, name, params=None):
        super(CADSA, self).__init__(name, params)

    def init_message_boxes(self, all_agents):
        # init_message_boxes(all_agents, iterations=2)
        pass

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
                if robot.num > robot_nei.num and robot.next_pos_node is robot_nei.next_pos_node:
                    robot_nei.next_pos_node = None

        for robot in robots:
            for robot_nei in robot.neighbours:
                if robot.next_pos_node is robot_nei.pos_node:
                    if robot_nei.next_pos_node is robot_nei.pos_node or robot_nei.next_pos_node is None:
                        robot.next_pos_node = None
                if robot_nei.next_pos_node is robot.pos_node:
                    if robot.next_pos_node is robot.pos_node or robot.next_pos_node is None:
                        robot_nei.next_pos_node = None

        for node in robots:
            node.prev_pos_node = node.pos_node
            if node.next_pos_node:
                node.pos_node = node.next_pos_node

        for node1 in robots:
            for node2 in robots:
                if node1.name != node2.name:
                    if node1.pos_node is node2.pos_node:
                        node1.pos_node = node1.prev_pos_node
                        node2.pos_node = node2.prev_pos_node
                        print('collision')













