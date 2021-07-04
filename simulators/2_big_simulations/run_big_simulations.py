from processes import *
from tracker import tracker
from simulators.algorithms.algorithms import *


def main():
    start = time.time()
    dict_for_results, dict_for_plots = create_measurement_dicts(ALGORITHMS_TO_CHECK)
    fig, ax = plt.subplots(figsize=[6.4, 6.4])

    targets = create_targets()
    robots = create_robots()

    for problem in range(B_NUMBER_OF_PROBLEMS):
        graph = create_graph()
        initialize_start_positions(graph, robots, targets)

        for alg_num, (alg_name, params) in enumerate(ALGORITHMS_TO_CHECK):
            algorithm = get_the_algorithm_object(alg_name)
            reset_agents(graph, robots, targets, algorithm)

            for iteration in range(B_ITERATIONS_IN_BIG_LOOPS):
                send_messages(iteration, graph, robots, targets, algorithm)
                move_to_new_positions(iteration, graph, robots, targets, algorithm)

                tracker.step(problem, alg_num, iteration)
                plot_field(graph, robots, targets, fig, ax)
                choices = print_and_return_choices(all_agents=[*graph, *robots, *robots], iteration=iteration)
                # update_statistics(dict_for_results, dict_for_plots, all_agents, choices, algorithm,
                #                   iteration=iteration, problem=problem)

    print_minutes(start)
    # pickle_results(graphs, results_dict)
    plot_results()


if __name__ == '__main__':
    main()
