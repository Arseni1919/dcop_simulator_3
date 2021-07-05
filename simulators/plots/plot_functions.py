import matplotlib.pyplot as plt

from simulators.functions import *

lines = ['-', '--', '-.', ':', ]
lines.reverse()
markers = ['o', '+', '.', ',', '_', '*']
markers.reverse()


def plot_position_choices(all_agents, collisions):
    """
    Here we can see collisions inside a graph
    :param all_agents: [agent1, agent2, ...]
    :param collisions: [{'robot_name': ['pos_i', ...], 'robot_name_2': ['pos_i', ...], ...}, ...]
    :return: None
    """
    fig1, ax1 = plt.subplots()  # figsize=[6.4, 6.4]
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
        ax1.plot(plot_dict_x[robot_name], position_nums, 'o-', label=robot_name, alpha=0.5)

    ax1.legend()
    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Positions')
    if len(position_objects) < 20:
        ax1.set_yticks([x.num for x in position_objects])
    ax1.set_xticks(list(range(len(collisions))))
    plt.show()


def plot_positions_graph(graph):
    # plt.clf()
    plt.rcParams["figure.figsize"] = [6.4, 6.4]
    # node points of the graph
    plt.scatter(
        [pos_node.pos_node[0] for pos_node in graph],
        [pos_node.pos_node[1] for pos_node in graph]
    )

    for pos_node in graph:
        plt.annotate(pos_node.num, pos_node.pos_node, fontsize=7)

    # edge lines on the graph
    for pos_node in graph:
        x_edges_list, y_edges_list = [], []
        for nearby_node_name, nearby_node in pos_node.nearby_position_nodes.items():
            x_edges_list.extend([pos_node.pos_node[0], nearby_node.pos_node[0]])
            y_edges_list.extend([pos_node.pos_node[1], nearby_node.pos_node[1]])
        plt.plot(x_edges_list, y_edges_list, alpha=0.5)

    plt.show()


# ------------ ADD ------------ #
def add_graph(to_ax, line_index, marker_index, graph_dict, matrix_name, dimension_to_avrg, alg_name, alg_label, color):
    if alg_name in graph_dict:
        print(colored(f'There {alg_name} is inside the dictionary.', 'green'))
        line_index = 0 if line_index == len(lines) else line_index
        marker_index = 0 if marker_index == len(markers) else marker_index
        matrix = graph_dict[alg_name][matrix_name]
        avr = np.average(matrix, dimension_to_avrg)
        std = np.std(matrix, dimension_to_avrg)
        line = lines[line_index]
        marker = markers[marker_index]
        print(f'{alg_name}: li:{line_index} mi:{marker_index}')
        to_ax.plot(range(len(avr)), avr, '%s%s' % (marker, line), label=alg_label, color=color)

        to_ax.fill_between(range(len(avr)), avr - AMOUNT_OF_STD * std, avr + AMOUNT_OF_STD * std,
                           alpha=0.2, antialiased=True, color=color)
    else:
        print(colored(f'There {alg_name} is not inside the dictionary.', 'red'))


# ----------------------------- #



















