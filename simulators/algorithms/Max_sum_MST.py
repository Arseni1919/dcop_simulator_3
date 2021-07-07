from simulators.algorithms.CAMS import *


class Max_sum_MST(CAMS):
    name = 'Max_sum_MST'

    def __init__(self, name, params=None):
        super(CAMS, self).__init__(name, params)

    def init_nodes_before_big_loops(self,
                                    graph: List[BigSimulationPositionNode],
                                    robots: List[BigSimulationRobotNode],
                                    targets: List[BigSimulationTargetNode]):
        # print('in init_nodes_before_big_loops')
        if 'diff_creds' in self.params:
            set_diff_cred(robots, self.params['diff_creds']['min'], self.params['diff_creds']['max'])

    def init_nodes_before_small_loops(self,
                                      graph: List[BigSimulationPositionNode],
                                      robots: List[BigSimulationRobotNode],
                                      targets: List[BigSimulationTargetNode]):
        # print('in init_nodes_before_small_loops')
        # update robots domains
        _ = [robot.update_domain() for robot in robots]

        # update targets cells_near_me
        _ = [target.update_cells_near_me(robots, graph) for target in targets]

        # clean neighbours
        _ = [agent.clean_neighbours() for agent in [*graph, *robots, *targets]]

        # neighbours - Targets and Robots
        self.add_nei_targets_robots(targets, robots)

        # FMR
        self.FMR_correction(targets)

        # init message boxes
        init_message_boxes([*robots, *targets], B_ITERATIONS_IN_SMALL_LOOPS)

    def send_messages(self, big_iteration, graph, robots, targets, problem, alg_num, tracker):
        for iteration in range(B_ITERATIONS_IN_SMALL_LOOPS):
            all_agents = [*robots, *targets]
            for agent in all_agents:
                tracker.step(problem, alg_num, big_iteration, iteration, agent)
                for nei in agent.neighbours:
                    agent.send_message_to(nei, iteration)

            tracker.step(problem, alg_num, big_iteration, iteration)

    def add_nei_positions_robots(self, graph, robots):
        pass






































