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
def add_graph(to_ax, line_index, marker_index, graph_dict, matrix_name, dimension_to_avrg, alg_name, alg_label, color,
              need_to_plot_variance=True):
    if alg_name in graph_dict:
        print(colored(f'There {alg_name} is inside the dictionary.', 'green'))
        # line_index = 0 if line_index == len(lines) else line_index
        # marker_index = 0 if marker_index == len(markers) else marker_index
        matrix = graph_dict[alg_name][matrix_name]
        avr = np.average(matrix, dimension_to_avrg)
        std = np.std(matrix, dimension_to_avrg)
        # line = lines[line_index]
        # marker = markers[marker_index]
        # print(f'{alg_name}: li:{line_index} mi:{marker_index}')
        to_ax.plot(range(len(avr)), avr, '%s%s' % (line_index, marker_index), label=alg_label, color=color)
        if SHOW_RANGES:
            to_ax.fill_between(range(len(avr)), avr - AMOUNT_OF_STD * std, avr + AMOUNT_OF_STD * std,
                               alpha=0.2, antialiased=True, color=color)
    else:
        print(colored(f'There {alg_name} is not inside the dictionary.', 'red'))


def add_list_of_graphs(ax, results_dict, matrix_name):
    # lines = ['-', '--', '-.', ':', ]
    # lines.reverse()
    # markers = ['o', '+', '.', ',', '_', '*']
    # markers.reverse()
    # add_graph(to_ax, line_index, marker_index, graph_dict, matrix_name, dimension_to_avrg, alg_name, alg_label, color, need_to_plot_variance=True)
    dim=1
    add_graph(ax, ':', '*', results_dict, matrix_name, dim, 'Random-Walk', 'Random-Walk', 'b')

    add_graph(ax, '-', '1', results_dict, matrix_name, dim, 'DSA_MST', 'DSA_MST', 'tab:blue')
    add_graph(ax, '--', '1', results_dict, matrix_name, dim, 'CADSA', 'CADSA', 'tab:cyan')
    add_graph(ax, ':', '1', results_dict, matrix_name, dim, 'DSSA', 'DSSA', 'tab:purple')

    # add_graph(ax, '-', "+", results_dict, matrix_name, dim, 'Max_sum_MST', 'Max-sum_MST', 'tab:brown')
    add_graph(ax, '--', "+", results_dict, matrix_name, dim, 'Max_sum_MST_delta', 'Max-sum_MST', 'goldenrod')
    # add_graph(ax, ':', "+", results_dict, matrix_name, dim, 'Max_sum_MST_delta_from_single', 'Max-sum_MST (delta 2)', 'darkred')
    add_graph(ax, '-.', "+", results_dict, matrix_name, dim, 'Max-sum_MST_breakdowns', 'Max-sum_MST\n(including breakdowns)', 'tomato')

    # add_graph(ax, '-.', ".", results_dict, matrix_name, dim, 'CAMS', 'CAMS', 'indigo')
    add_graph(ax, '--', ".", results_dict, matrix_name, dim, 'CAMS_delta', 'CAMS', 'tab:pink')
    # add_graph(ax, ':', ".", results_dict, matrix_name, dim, 'CAMS_delta_from_single', 'CAMS (delta 2)', 'm')

    # add_graph(ax, 0, 1, results_dict, matrix_name, dim, 'Random-Walk_breakdowns', 'Random-Walk\n(including breakdowns)', 'tab:olive')
    # add_graph(ax, 3, 0, results_dict, matrix_name, dim, 'DSA_MST_breakdowns', 'DSA_MST\n(including breakdowns)', 'tab:purple')
    # add_graph(ax, 3, 1, results_dict, matrix_name, dim, 'CAMS_breakdowns', 'CAMS\n(including breakdowns)', 'tab:gray')
    # add_graph(ax, 1, 4, results_dict, matrix_name, dim, 'CAMS_diff_creds', 'CAMS_diff_creds', 'g')

# ----------------------------- #



















