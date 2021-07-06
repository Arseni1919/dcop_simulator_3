from processes import *
from tracker import tracker
from simulators.algorithms.algorithms import *


def main():
    start = time.time()
    dict_for_results = create_measurement_dicts()
    fig, ax = create_fig_ax()

    targets = create_targets()
    robots = create_robots()

    for problem in range(B_NUMBER_OF_PROBLEMS):
        graph = create_graph(dict_for_results, problem)
        initialize_start_positions(graph, robots, targets)

        for alg_num, (alg_name, params) in enumerate(ALGORITHMS_TO_CHECK):
            reset_agents(graph, robots, targets)
            algorithm = get_the_algorithm_object(alg_name)
            algorithm.init_nodes_before_big_loops(graph, robots, targets)

            for big_iteration in range(B_ITERATIONS_IN_BIG_LOOPS):
                algorithm.init_nodes_before_small_loops(graph, robots, targets)
                algorithm.send_messages(big_iteration, graph, robots, targets, problem, alg_num, tracker)
                algorithm.move(graph, robots, targets)

                tracker.step(problem, alg_num, big_iteration)
                plot_field(graph, robots, targets, fig, ax)
                update_statistics(graph, robots, targets, big_iteration, algorithm, problem, dict_for_results)

    print_minutes(start)
    file_name = pickle_results(dict_for_results)
    print_and_plot_results(file_name)


if __name__ == '__main__':
    main()
