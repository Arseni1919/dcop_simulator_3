from simulators.nodes import *
from simulators.algorithms.algorithms import *


def create_measurement_dicts(algorithms):
    # dict_for_results = {'alg_name': {'col': [], 'new_positions': []}}
    # dict_for_plots[algorithm][iteration][problem] = convergence
    dict_for_results = {}
    dict_for_plots = {}
    for alg_name, params in algorithms:
        dict_for_results[alg_name] = {'col': [], 'new_positions': []}
        dict_for_plots[alg_name] = np.zeros((B_ITERATIONS_IN_BIG_LOOPS, B_NUMBER_OF_PROBLEMS))
    return dict_for_results, dict_for_plots


def create_graph():
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

    return graph


def plot_results(robots, targets, collisions):
    # print_results(results_dict)
    # plot_collisions(results_dict)
    # plot_results_if(graphs)
    # print_t_test(graphs)
    # plot_positions_graph(graph)

    pass


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


def reset_delay(x):
    x.delay = 0


def reset_agents(graph, robots, targets, algorithm: MetaAlgorithm):
    list(map(init_pos, robots))
    list(map(reset_delay, robots))


def move_to_new_positions(iteration, graph, robots, targets, algorithm: MetaAlgorithm):
    list(map(algorithm.move, robots))


def update_statistics(graph, robots, targets,
                      collisions: list,
                      choices,
                      dict_for_results,
                      dict_for_plots,
                      algorithm,
                      iteration,
                      problem):
    collisions.append(choices)
    # plot_position_choices([*graph, *robots, *targets], collisions)


def initialize_start_positions(graph, robots, targets):
    pos_to_robots = random.sample(graph, len(robots) + len(targets))
    for pos_node, agent in zip(pos_to_robots, [*robots, *targets]):
        agent.pos_node = pos_node
        agent.initial_pos_node = pos_node


def plot_field(graph, robots, targets, fig, ax):
    # fig.clf()
    ax.clear()
    padding = 4
    ax.set_xlim([0 - padding, B_WIDTH + padding])
    ax.set_ylim([0 - padding, B_WIDTH + padding])

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
        circle1 = plt.Circle(robot.pos_node.pos, B_SIZE_ROBOT_NODE, color='b', alpha=0.3)
        ax.add_patch(circle1)
        ax.annotate(robot.name, robot.pos_node.pos, fontsize=5)

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


def pickle_results(dict_for_results, dict_for_plots):
    if PICKLE_RESULTS:
        pass
