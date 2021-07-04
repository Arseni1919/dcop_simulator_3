from processes import *
from tracker import tracker
from simulators.algorithms.algorithms import *


def main():
    start = time.time()
    dict_for_results, dict_for_plots = create_measurement_dicts(ALGORITHMS_TO_CHECK)
    collisions = []
    fig, ax = plt.subplots(figsize=[6.4, 6.4])

    targets = create_targets()
    robots = create_robots()

    for problem in range(B_NUMBER_OF_PROBLEMS):
        graph = create_graph()
        initialize_start_positions(graph, robots, targets)

        for alg_num, (alg_name, params) in enumerate(ALGORITHMS_TO_CHECK):
            algorithm = get_the_algorithm_object(alg_name)
            reset_agents(graph, robots, targets, algorithm)
            algorithm.init_nodes_before_big_loops(graph, robots, targets)

            for iteration in range(B_ITERATIONS_IN_BIG_LOOPS):
                algorithm.init_nodes_before_small_loops(graph, robots, targets)
                algorithm.send_messages(iteration, graph, robots, targets)
                move_to_new_positions(iteration, graph, robots, targets, algorithm)

                tracker.step(problem, alg_num, iteration)
                plot_field(graph, robots, targets, fig, ax)
                choices = print_and_return_choices(all_agents=[*graph, *robots, *robots], iteration=iteration)
                update_statistics(graph, robots, targets, collisions, choices,
                                  dict_for_results, dict_for_plots, algorithm, iteration, problem)  # !

    print_minutes(start)
    pickle_results(dict_for_results, dict_for_plots)
    plot_results(robots, targets, collisions=collisions)


if __name__ == '__main__':
    main()
