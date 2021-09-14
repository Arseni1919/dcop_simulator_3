from simulators.algorithms.Max_sum_MST import *


class CAMS(Max_sum_MST):
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

    def init_nodes_before_small_loops(self,
                                      graph: List[BigSimulationPositionNode],
                                      robots: List[BigSimulationRobotNode],
                                      targets: List[BigSimulationTargetNode]):
        # print('in init_nodes_before_small_loops')
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

        # update dict_of_weights
        _ = [pos_node.update_dict_of_weights(robots) for pos_node in graph]

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
                    agent.send_message_to(nei, iteration, params=self.params)

            tracker.step(problem, alg_num, big_iteration, iteration)
            # print_table_of_messages(all_agents, iteration)
            # input()
        # input()

    def add_nei_positions_robots(self, graph, robots):
        pos_nodes_dict = {pos_node.name: pos_node for pos_node in graph}
        for robot in robots:
            for pos_node_name in robot.domain:
                pos_node = pos_nodes_dict[pos_node_name]
                pos_node.neighbours.append(robot)
                robot.neighbours.append(pos_node)













