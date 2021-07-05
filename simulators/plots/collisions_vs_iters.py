from simulators.plots.plot_functions import *


def plot_collisions_vs_iters(file_name):
    results_dict = load_file(file_name)
    fig, ax = plt.subplots()
    # add_graph(to_ax, line_index, marker_index, graph_dict, matrix_name, dimension_to_avrg, alg_name, alg_label, color)
    matrix_name = 'collisions'
    dim = 1
    add_graph(ax, 0, 0, results_dict, matrix_name, dim, 'Random-Walk', 'Random-Walk', 'b')
    add_graph(ax, 3, 4, results_dict, matrix_name, dim, 'DSA_MST', 'DSA_MST', 'tab:brown')
    add_graph(ax, 3, 0, results_dict, matrix_name, dim, 'DSA_MST', 'DSA_MST\n(including breakdowns)', 'tab:purple')
    add_graph(ax, 3, 3, results_dict, matrix_name, dim, 'DSA_MST', 'CADSA', 'tab:cyan')
    add_graph(ax, 1, 4, results_dict, matrix_name, dim, 'Max-sum_MST', 'Max-sum_MST', 'g')
    add_graph(ax, 1, 2, results_dict, matrix_name, dim, 'Max-sum_MST', 'Max-sum_MST\n(including breakdowns)', 'tab:orange')
    add_graph(ax, 2, 1, results_dict, matrix_name, dim, 'CAMS', 'CAMS', 'm')

    # ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 15})
    # ax.set_title('Collisions')
    ax.set_ylabel('Collisions', fontsize=18)
    ax.set_xlabel('Iterations', fontsize=18)
    # ax.set_xticks(iterations)
    # ax.set_xlim(xmin=iterations[0], xmax=iterations[-1])
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_collisions_vs_iters()











