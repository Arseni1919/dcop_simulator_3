import matplotlib.pyplot as plt

from simulators.nodes import *
from simulators.algorithms.algorithms import *
from simulators.plots.coverage_vs_iters import *
from simulators.plots.collisions_vs_iters import *

# from simulators.constants_and_packages import *


def create_graph(dict_for_results, problem):
    graph = []
    x_list = [np.random.uniform(0, B_WIDTH) for _ in range(B_N_NODES)]
    y_list = [np.random.uniform(0, B_WIDTH) for _ in range(B_N_NODES)]
    xy = np.array(list(zip(x_list, y_list)))
    nbrs = NearestNeighbors(n_neighbors=B_MAX_NEARBY_POS + 1, algorithm='ball_tree').fit(xy)
    dists, indcs = nbrs.kneighbors(xy)

    for pos_indx, pos in enumerate(xy):
        graph.append(BigSimulationPositionNode(f'pos{pos_indx}', pos_indx, dict_of_weights={}, pos=pos))

    for node, indc_list in enumerate(indcs):
        self_pos = graph[indc_list[0]]
        n_nei = random.randint(B_MIN_NEARBY_POS, B_MAX_NEARBY_POS)
        for j, nei in enumerate(indc_list[1:n_nei]):
            if dists[node][j + 1] < B_MAX_DISTANCE_OF_NEARBY_POS:
                nearby_pos = graph[nei]
                if len(self_pos.nearby_position_nodes) < B_MAX_NEARBY_POS:
                    if len(nearby_pos.nearby_position_nodes) < B_MAX_NEARBY_POS:
                        self_pos.nearby_position_nodes[nearby_pos.name] = nearby_pos
                        nearby_pos.nearby_position_nodes[self_pos.name] = self_pos
    dict_for_results['problems'][problem] = graph
    return graph


def print_t_test(file_name):
    results_dict = load_file(file_name)
    length_of_name = min([len(x) for x, y in ALGORITHMS_TO_CHECK])
    for alg_name1, _ in ALGORITHMS_TO_CHECK:
        matrix1 = results_dict[alg_name1]['coverage']
        for alg_name2, _ in ALGORITHMS_TO_CHECK:
            if alg_name1 != alg_name2:
                matrix2 = results_dict[alg_name2]['coverage']
                print(f'{alg_name1[:length_of_name]} <-> {alg_name2[:length_of_name]} '
                      f'\tP_value: {ttest_ind(matrix1[-1], matrix2[-1])[1]: 10.2f}')


def print_and_plot_results(file_name):
    plt.close()
    print('Plotting the results...')
    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)
    print_t_test(file_name)


def create_targets():
    targets = [
        BigSimulationTargetNode(f'target{i}', i, req=100)
        for i in range(B_NUM_OF_TARGETS)
    ]
    return targets


def create_robots():
    robots = [
        BigSimulationRobotNode(f'robot{i}', i, cred=30)
        for i in range(B_NUM_OF_ROBOTS)
    ]
    return robots


def init_pos(x):
    x.pos_node = x.initial_pos_node
    x.prev_pos_node = None
    x.next_pos_node = None


def reset_delay(x):
    x.delay = 0


def reset_agents(graph, robots, targets):
    list(map(init_pos, robots))
    list(map(reset_delay, robots))
    return graph[:], robots[:], targets[:]


def move_to_new_positions(iteration, graph, robots, targets, algorithm: MetaAlgorithm):
    pass


def create_measurement_dicts():
    """
    :return: dict_for_results = {
        'alg_name': {
            'coverage': matrix[iteration][problem] = coverage,
            'collisions': matrix[iteration][problem] = collisions,
            'positions': {
                iteration: {
                    problem: {
                        'agent_name (robot, target)': 'pos_name'
                    }
                }
            }
        }
    }
    """
    dict_for_results = {}
    for alg_name, params in ALGORITHMS_TO_CHECK:
        positions_dict = {
            itr: {
                problem_i: {} for problem_i in range(B_NUMBER_OF_PROBLEMS)
            }
            for itr in range(B_ITERATIONS_IN_BIG_LOOPS)
        }

        dict_for_results[alg_name] = {
            'coverage': np.zeros((B_ITERATIONS_IN_BIG_LOOPS, B_NUMBER_OF_PROBLEMS)),
            'collisions': np.zeros((B_ITERATIONS_IN_BIG_LOOPS, B_NUMBER_OF_PROBLEMS)),
            'positions': positions_dict,
            'params': params,
        }
        dict_for_results['problems'] = {i: 0 for i in range(B_NUMBER_OF_PROBLEMS)}

    return dict_for_results


def update_statistics(graph, robots, targets, big_iteration, algorithm, problem, dict_for_results):
    """
    Update dict_for_results.
    :param graph: list
    :param robots: list
    :param targets: list
    :param choices:
    :param big_iteration:
    :param algorithm:
    :param problem:
    :param dict_for_results: {
        'alg_name': {
            'coverage': matrix[iteration][problem] = coverage,
            'collisions': matrix[iteration][problem] = collisions,
            'positions': {
                iteration: {
                    problem: {
                        'agent_name (robot, target)': 'pos_name'
                    }
                }
            }
        }
    }
    :return:
    """
    dict_for_results[algorithm.name]['coverage'][big_iteration][problem] = calculate_coverage(robots, targets)
    dict_for_results[algorithm.name]['collisions'][big_iteration][problem] = calculate_collisions(robots, big_iteration)

    choices = print_and_return_choices(all_agents=[*graph, *robots, *robots])
    dict_for_results[algorithm.name]['positions'][big_iteration][problem] = choices
    # dict_for_results['problems'][problem] = graph


def initialize_nodes_before_algorithms(graph, robots, targets):
    pos_to_robots = random.sample(graph, len(robots) + len(targets))
    for pos_node, agent in zip(pos_to_robots, [*robots, *targets]):
        agent.pos_node = pos_node
        agent.initial_pos_node = pos_node

    if DIFF_CRED:
        set_diff_cred(robots, MIN_CRED, MAX_CRED)


def create_fig_ax():
    if NEED_TO_PLOT_FIELD:
        return plt.subplots(figsize=[6.4, 6.4])
    else:
        return 0, 0


def plot_field(graph, robots, targets, alg_name, problem, big_iteration, fig, ax):
    if NEED_TO_PLOT_FIELD:
        # fig.clf()
        ax.clear()
        padding = 4
        ax.set_xlim([0 - padding, B_WIDTH + padding])
        ax.set_ylim([0 - padding, B_WIDTH + padding])

        # title
        ax.set_title(
            f'{alg_name} '
            f'\nProblem:({problem+1}/{B_NUMBER_OF_PROBLEMS}) Iteration: ({big_iteration+1}/{B_ITERATIONS_IN_BIG_LOOPS})'
        )

        # POSITIONS
        ax.scatter(
            [pos_node.pos[0] for pos_node in graph],
            [pos_node.pos[1] for pos_node in graph],
            color='g', alpha=0.3, marker="s"
        )

        # POSITION ANNOTATIONS
        # for pos_node in graph:
        #     ax.annotate(pos_node.num, pos_node.pos, fontsize=5)

        # EDGES: edge lines on the graph
        for pos_node in graph:
            x_edges_list, y_edges_list = [], []
            for nearby_node_name, nearby_node in pos_node.nearby_position_nodes.items():
                x_edges_list.extend([pos_node.pos[0], nearby_node.pos[0]])
                y_edges_list.extend([pos_node.pos[1], nearby_node.pos[1]])
            plt.plot(x_edges_list, y_edges_list, color='g', alpha=0.3)

        # ROBOTS
        for robot in robots:
            # robot
            circle1 = plt.Circle(robot.pos_node.pos, B_SIZE_ROBOT_NODE, color='b', alpha=0.3)
            ax.add_patch(circle1)
            ax.annotate(robot.name, robot.pos_node.pos, fontsize=5)

            # range of sr
            circle_sr = plt.Circle(robot.pos_node.pos, robot.sr, color='y', alpha=0.05)
            ax.add_patch(circle_sr)

            # range of mr
            circle_mr = plt.Circle(robot.pos_node.pos, robot.mr, color='tab:purple', alpha=0.05)
            ax.add_patch(circle_mr)

        # TARGETS
        for target in targets:
            rect = plt.Rectangle(target.pos_node.pos - (B_SIZE_TARGET_NODE / 2, B_SIZE_TARGET_NODE / 2), B_SIZE_TARGET_NODE,
                                 B_SIZE_TARGET_NODE, color='r', alpha=0.3)
            ax.add_patch(rect)
            ax.annotate(target.name, target.pos_node.pos, fontsize=5)

        # light up nodes upon the changes
        if LIGHT_UP_THE_CHANGES:
            pass

        plt.pause(0.05)


def pickle_results(dict_for_results):
    if PICKLE_RESULTS:
        try:
            time_suffix_str = time.strftime("%d.%m.%Y-%H:%M:%S")
            file_name = f'results/{time_suffix_str}_{ADDING_TO_FILE_NAME}.results'
            # open the file for writing
            with open(file_name, 'wb') as fileObject:
                pickle.dump(dict_for_results, fileObject)
            print('Pickled successfully!')
            return file_name
        except RuntimeError:
            print('[ERROR] Pickle failed!')
    return None
