from simulators.plots.plot_functions import *


def plot_collisions_vs_iters(file_name):
    results_dict = load_file(file_name)
    fig, ax = plt.subplots()
    # add_graph(to_ax, line_index, marker_index, graph_dict, matrix_name, dimension_to_avrg, alg_name, alg_label, color)
    add_list_of_graphs(ax, results_dict, 'collisions')
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
    plot_collisions_vs_iters('')











