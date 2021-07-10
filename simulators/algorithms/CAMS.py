import random
from typing import List
from simulators.algorithms.MetaAlgorithm import *
from simulators.nodes import *


class CAMS(MetaAlgorithm):
    name = 'CAMS'

    def __init__(self, name, params=None):
        super(CAMS, self).__init__(name, params)

    def init_nodes_before_big_loops(self,
                                    graph: List[BigSimulationPositionNode],
                                    robots: List[BigSimulationRobotNode],
                                    targets: List[BigSimulationTargetNode]):
        # print('in init_nodes_before_big_loops')
        # update dict_of_weights
        _ = [pos_node.update_dict_of_weights(robots) for pos_node in graph]
        # if 'diff_creds' in self.params:
        #     set_diff_cred(robots, self.params['diff_creds']['min'], self.params['diff_creds']['max'])
        pass


    def init_nodes_before_small_loops(self,
                                      graph: List[BigSimulationPositionNode],
                                      robots: List[BigSimulationRobotNode],
                                      targets: List[BigSimulationTargetNode]):
        # print('in init_nodes_before_small_loops')
        # update dict_of_weights
        _ = [pos_node.update_dict_of_weights(robots) for pos_node in graph]

        # update robots domains
        _ = [robot.update_domain_and_reset_next_pose_node() for robot in robots]

        # update targets cells_near_me
        _ = [target.update_cells_near_me(robots, graph) for target in targets]

        # clean neighbours
        _ = [agent.clean_neighbours() for agent in [*graph, *robots, *targets]]

        # neighbours - Targets and Robots
        self.add_nei_targets_robots(targets, robots)

        # FMR
        self.FMR_correction(targets)

        # neighbours - Positions and Robots
        self.add_nei_positions_robots(graph, robots)

        # init message boxes
        init_message_boxes([*graph, *robots, *targets], B_ITERATIONS_IN_SMALL_LOOPS)

    def send_messages(self, big_iteration, graph, robots, targets, problem, alg_num, tracker):
        for iteration in range(B_ITERATIONS_IN_SMALL_LOOPS):
            all_agents = [*graph, *robots, *targets]
            for agent in all_agents:
                tracker.step(problem, alg_num, big_iteration, iteration, agent)
                for nei in agent.neighbours:
                    agent.send_message_to(nei, iteration)

            tracker.step(problem, alg_num, big_iteration, iteration)

    def send_message(self, from_node, to_node):
        raise RuntimeError

    def move(self, graph, robots, targets):
        pos_nodes_dict = {pos_node.name: pos_node for pos_node in graph}
        # choices: {'robot_name': ['pos_i', ...], 'robot_name_2': ['pos_i', ...], ...}
        choices = print_and_return_choices([*graph, *robots, *targets], B_ITERATIONS_IN_SMALL_LOOPS-1)
        for robot in robots:
            list_of_robot_choices = choices[robot.name]
            next_position = pos_nodes_dict[random.sample(list_of_robot_choices, 1)[0]]
            robot.prev_pos_node = robot.pos_node
            robot.pos_node = next_position

        self.breakdowns_correction(robots)

    def breakdowns_correction(self, robots):
        breakdowns_correction(robots, self.params)

    def add_nei_targets_robots(self, targets, robots):
        for robot in robots:
            for target in targets:
                in_range = [pos_node_name in target.cells_near_me for pos_node_name in robot.domain]
                if any(in_range):
                    target.neighbours.append(robot)
                    robot.neighbours.append(target)

    def add_nei_positions_robots(self, graph, robots):
        pos_nodes_dict = {pos_node.name: pos_node for pos_node in graph}
        for robot in robots:
            for pos_node_name in robot.domain:
                pos_node = pos_nodes_dict[pos_node_name]
                pos_node.neighbours.append(robot)
                robot.neighbours.append(pos_node)

    def FMR_correction(self, targets):
        for target in targets:
            target.fmr_set = select_FMR_nei(target)
            for robot in target.neighbours[:]:
                if robot not in target.fmr_set:
                    target.neighbours.remove(robot)
                    robot.neighbours.remove(target)


CAMS_alg = CAMS('CAMS')












