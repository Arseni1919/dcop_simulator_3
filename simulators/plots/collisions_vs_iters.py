from simulators.plots.plot_functions import *


def plot_collisions_vs_iters(file_name):
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
    results_dict = load_file(file_name)
    fig, ax = plt.subplots()

    for k_res_dict, v_res_dict in results_dict.items():
        if type(v_res_dict) is dict and 'collisions' in v_res_dict:
            collisions = v_res_dict['collisions']
            cum_collisions = np.cumsum(collisions, axis=0)
            v_res_dict['cum_collisions'] = cum_collisions

    # add_graph(to_ax, line_index, marker_index, graph_dict, matrix_name, dimension_to_avrg, alg_name, alg_label, color)
    add_list_of_graphs(ax, results_dict, 'cum_collisions')
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















    # for alg_name in algs:
    #     for rd in results_dict_list:
    #         try:
    #             curr_col_list_yd = rd[alg_name]['col']
    #             chunks = [curr_col_list_yd[x:x + iterations] for x in range(0, len(curr_col_list_yd), iterations)]
    #             rd[alg_name] = np.array([np.cumsum(x) for x in chunks])
    #         except:
    #             print(alg_name)
    #     print()

    # if matrix_name == 'collisions':
    #     avr = np.cumsum(matrix, dimension_to_avrg)
    #     std = np.std(matrix, dimension_to_avrg)
    # else:
    #     avr = np.average(matrix, dimension_to_avrg)
    #     std = np.std(matrix, dimension_to_avrg)











