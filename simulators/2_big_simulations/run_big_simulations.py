from processes import *
from tracker import tracker
from simulators.algorithms.algorithms import *


def main():
    tracker.print_start_of_simulation_time()
    start = time.time()
    dict_for_results = create_measurement_dicts()
    fig, ax = create_fig_ax()

    targets = create_targets()
    robots = create_robots()
    check_algorithms()

    for problem in range(B_NUMBER_OF_PROBLEMS):
        graph = create_graph(dict_for_results, problem)
        initialize_nodes_before_algorithms(graph, robots, targets)

        for alg_num, (alg_name, params) in enumerate(ALGORITHMS_TO_CHECK):
            i_graph, i_robots, i_targets = reset_agents(graph, robots, targets)
            algorithm = get_the_algorithm_object(alg_name, params)
            algorithm.init_nodes_before_big_loops(i_graph, i_robots, i_targets)

            for big_iteration in range(B_ITERATIONS_IN_BIG_LOOPS):
                algorithm.init_nodes_before_small_loops(i_graph, i_robots, i_targets)
                algorithm.send_messages(big_iteration, i_graph, i_robots, i_targets, problem, alg_num, tracker)
                algorithm.move(i_graph, i_robots, i_targets)

                tracker.step(problem, alg_num, big_iteration)
                plot_field(i_graph, i_robots, i_targets, alg_name, alg_num, problem, big_iteration, start, fig, ax)
                update_statistics(i_graph, i_robots, i_targets, big_iteration, algorithm, problem, dict_for_results)

    end = time.time()
    file_name = pickle_results(dict_for_results, start, end)
    print_and_plot_results(file_name)
    print_minutes(start, end)


if __name__ == '__main__':
    main()
