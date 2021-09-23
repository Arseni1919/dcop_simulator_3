import matplotlib.pyplot as plt

from simulators.nodes import *
from simulators.algorithms.algorithms import *
from simulators.plots.coverage_vs_iters import *
from simulators.plots.collisions_vs_iters import *
from tracker import tracker
# from simulators.constants_and_packages import *


def create_complex_graph():
    graph = []
    x_list = [np.random.uniform(0, B_WIDTH) for _ in range(B_N_NODES)]
    y_list = [np.random.uniform(0, B_HEIGHT) for _ in range(B_N_NODES)]
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
    return graph


def create_grid_graph():
    graph = []
    padding_w = B_WIDTH / GRID_SIZE_SIDE_WH
    padding_h = B_HEIGHT / GRID_SIZE_SIDE_WH
    pos_indx = 0
    for row in range(GRID_SIZE_SIDE_WH):
        for column in range(GRID_SIZE_SIDE_WH):
            pos = np.asarray([row * padding_w, column * padding_h])
            graph.append(BigSimulationPositionNode(f'pos{pos_indx}', pos_indx, dict_of_weights={}, pos=pos))
            pos_indx += 1

    for self_pos in graph:
        for another_pos in graph:
            is_neighbour = False
            # UP
            if (self_pos.pos[0] == another_pos.pos[0]
                and abs(self_pos.pos[1] - another_pos.pos[1]) == padding_h) \
                    or (self_pos.pos[1] == another_pos.pos[1]
                        and abs(self_pos.pos[0] - another_pos.pos[0]) == padding_w):
                is_neighbour = True
            if is_neighbour:
                self_pos.nearby_position_nodes[another_pos.name] = another_pos
                another_pos.nearby_position_nodes[self_pos.name] = self_pos
    return graph


def create_graph(dict_for_results, problem):
    if GRAPH_TYPE == 'complex':
        graph = create_complex_graph()
    elif GRAPH_TYPE == 'grid':
        graph = create_grid_graph()
    else:
        raise ValueError('[ERROR]: No appropriate value of a GRAPH_TYPE constant.')

    dict_for_results['problems'][problem] = {
        cell.name: (cell.pos, [nei for nei in cell.nearby_position_nodes.keys()]) for cell in graph
    }
    return graph


def print_and_plot_results(file_name):
    plt.close()
    print('Plotting the results...')
    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)
    print_t_test(file_name)


def create_targets():
    targets = [
        BigSimulationTargetNode(f'target{i}', i, req=REQ_OF_TARGETS)
        for i in range(B_NUM_OF_TARGETS)
    ]
    return targets


def create_robots():
    robots = [
        BigSimulationRobotNode(f'robot{i}', i, cred=30)
        for i in range(B_NUM_OF_ROBOTS)
    ]
    return robots


def reset_agents(graph, robots, targets):
    _ = [x.reset() for x in robots]
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
        ...
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
        dict_for_results['time'] = 0
        dict_for_results['B_NUMBER_OF_PROBLEMS'] = B_NUMBER_OF_PROBLEMS
        dict_for_results['B_NUM_OF_ROBOTS'] = B_NUM_OF_ROBOTS
        dict_for_results['B_NUM_OF_TARGETS'] = B_NUM_OF_TARGETS
        dict_for_results['B_ITERATIONS_IN_BIG_LOOPS'] = B_ITERATIONS_IN_BIG_LOOPS
        dict_for_results['B_ITERATIONS_IN_SMALL_LOOPS'] = B_ITERATIONS_IN_SMALL_LOOPS
        # dict_for_results[''] =
        # dict_for_results[''] =

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
    collisions = calculate_collisions(robots, big_iteration)
    dict_for_results[algorithm.name]['collisions'][big_iteration][problem] = collisions
    if algorithm.name == 'CAMS':
        if collisions > 0:
            print(f'There are {collisions} collisions during the run of {algorithm.name} algorithm.')
    # dict_for_results[algorithm.name]['chosen_positions'][big_iteration][problem] = calculate_chosen_positions(robots)
    choices = print_and_return_choices(all_agents=[*graph, *robots, *targets], s_iteration=B_ITERATIONS_IN_SMALL_LOOPS-1)
    dict_for_results[algorithm.name]['positions'][big_iteration][problem] = choices
    # dict_for_results['problems'][problem] = graph


def initialize_nodes_before_algorithms(graph, robots, targets):
    if TARGETS_APART:
        chosen = random.sample(graph, len(robots))
        for pos_node, agent in zip(chosen, robots):
            agent.pos_node = pos_node
            agent.initial_pos_node = pos_node

        positioned_targets = []

        for target in targets:
            again = True
            while again:
                again = False
                curr_pos = random.sample(graph, 1)[0]
                for robot in robots:
                    if distance(robot.pos_node.pos, curr_pos.pos) == 0:
                        again = True
                        break
                for positioned_target in positioned_targets:
                    if distance(positioned_target.pos_node.pos, curr_pos.pos) < 2 * SR:
                        again = True
                        break
                if not again:
                    target.pos_node = curr_pos
                    target.initial_pos_node = curr_pos
                    positioned_targets.append(target)
                    # break
    else:
        pos_to_agents = random.sample(graph, len(robots) + len(targets))
        # print(f'need:{len(robots) + len(targets)} fact: {len(set(pos_to_agents))}')
        for pos_node, agent in zip(pos_to_agents, [*robots, *targets]):
            agent.pos_node = pos_node
            agent.initial_pos_node = pos_node

    if DIFF_CRED:
        set_diff_cred(robots, MIN_CRED, MAX_CRED)


def create_fig_ax():
    if NEED_TO_PLOT_FIELD:
        return plt.subplots(figsize=[6.5, 6.5])
    else:
        return 0, 0


def plot_field(graph, robots, targets, alg_name, alg_num, problem, big_iteration, start, fig, ax):
    if NEED_TO_PLOT_FIELD:
        # fig.clf()
        ax.clear()
        padding = 4
        ax.set_xlim([0 - padding, B_WIDTH + padding])
        ax.set_ylim([0 - padding, B_WIDTH + padding])

        # titles
        ax.set_title(
            f'Problem:({problem+1}/{B_NUMBER_OF_PROBLEMS})   Iteration: ({big_iteration+1}/{B_ITERATIONS_IN_BIG_LOOPS})'
            f'\n{alg_name} ({alg_num+1}/{len(ALGORITHMS_TO_CHECK)}) '
        )
        ax.set_xlabel(f'\nTime of the run: {time.strftime("%H:%M:%S", time.gmtime(time.time() - start))}')

        # POSITIONS
        ax.scatter(
            [pos_node.pos[0] for pos_node in graph],
            [pos_node.pos[1] for pos_node in graph],
            color='g', alpha=0.3, marker="s"
        )

        # POSITION ANNOTATIONS
        for pos_node in graph:
            ax.annotate(pos_node.num, pos_node.pos, fontsize=5)

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


def pickle_results(dict_for_results, start, end):
    if PICKLE_RESULTS:
        dict_for_results['time'] = time.strftime("%H:%M:%S", time.gmtime(end - start))
        try:
            time_suffix_str = time.strftime("%Y.%m.%d-%H:%M:%S")
            file_name = f'results/{time_suffix_str}_{ADDING_TO_FILE_NAME}.results'
            # open the file for writing
            with open(file_name, 'wb') as fileObject:
                pickle.dump(dict_for_results, fileObject)
            print(colored('Pickled successfully!', 'green'))
            return file_name
        except RuntimeError:
            print(colored('[ERROR] Pickle failed!', 'red'))
    return None


def check_algorithms():
    """
    Quick check of all algorithms. Here we run two iterations with each one to see if everything works correctly.
    """
    print(f'{colored("[MESSAGE] Quickly checking algorithms...", color="yellow")}\n')
    graph = create_graph({'problems': {1: []}}, 1)
    targets = create_targets()
    robots = create_robots()
    initialize_nodes_before_algorithms(graph, robots, targets)
    for alg_num, (alg_name, params) in enumerate(ALGORITHMS_TO_CHECK):
        i_graph, i_robots, i_targets = reset_agents(graph, robots, targets)
        algorithm = get_the_algorithm_object(alg_name, params)
        algorithm.init_nodes_before_big_loops(i_graph, i_robots, i_targets)

        for big_iteration in range(2):
            algorithm.init_nodes_before_small_loops(i_graph, i_robots, i_targets)
            algorithm.send_messages(big_iteration, i_graph, i_robots, i_targets, 1, alg_num, tracker)
            algorithm.move(i_graph, i_robots, i_targets)
    print(f'\r{colored("[MESSAGE] Finished quick check.", color="yellow")}\n')


def print_duration(i_graph, i_robots, i_targets):
    if NEED_TO_PRINT_DURATION:

        def print_mean_and_var(name, list_of_nodes):
            a = []
            for i in list_of_nodes:
                a.extend(i.times_to_send_message)
            print(f'{name} -> mean: {np.mean(a) * 10**3: .2f} ms, var: {np.var(a) * 10**3: .2f} ms')

        print(f'\nTime it takes to send messages:')
        print_mean_and_var('positions', i_graph)
        print_mean_and_var('targets', i_targets)
        print_mean_and_var('robots', i_robots)






























