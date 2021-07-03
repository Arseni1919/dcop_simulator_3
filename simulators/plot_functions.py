import matplotlib.pyplot as plt

from simulators.functions import *


def plot_position_choices(all_agents, collisions):
    """
    Here we can see collisions inside a graph
    :param all_agents: [agent1, agent2, ...]
    :param collisions: [{'robot_name': ['pos_i', ...], 'robot_name_2': ['pos_i', ...], ...}, ...]
    :return: None
    """
    robots = list(filter(lambda x: 'rob' in x.name, all_agents))
    plot_dict_y = {x.name: [] for x in robots}
    plot_dict_x = {x.name: [] for x in robots}

    position_objects = list(filter(lambda x: 'pos' in x.name, all_agents))
    position_dict = {x.name: x.num for x in position_objects}

    for iteration, robot_name_to_pos_dict in enumerate(collisions):
        for robot_name, position_names in robot_name_to_pos_dict.items():
            plot_dict_y[robot_name].extend([position_dict[x] for x in position_names])
            plot_dict_x[robot_name].extend([iteration for _ in position_names])

    for robot_name, position_nums in plot_dict_y.items():
        plt.plot(plot_dict_x[robot_name], position_nums, 'o-', label=robot_name, alpha=0.5)

    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Positions')
    plt.yticks([x.num for x in position_objects])
    plt.xticks(list(range(len(collisions))))
    plt.show()


def plot_positions_graph(graph):
    # plt.clf()
    plt.rcParams["figure.figsize"] = [6.4, 6.4]
    # node points of the graph
    plt.scatter(
        [pos_node.pos[0] for pos_node in graph],
        [pos_node.pos[1] for pos_node in graph]
    )

    for pos_node in graph:
        plt.annotate(pos_node.num, pos_node.pos, fontsize=5)

    # edge lines on the graph
    for pos_node in graph:
        x_edges_list, y_edges_list = [], []
        for nearby_node_name, nearby_node in pos_node.nearby_position_nodes.items():
            x_edges_list.extend([pos_node.pos[0], nearby_node.pos[0]])
            y_edges_list.extend([pos_node.pos[1], nearby_node.pos[1]])
        plt.plot(x_edges_list, y_edges_list, alpha=0.5)

    plt.show()








