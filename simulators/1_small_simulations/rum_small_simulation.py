from scenarios import *
from processes import *
from simulators.plots.plot_functions import *


def main():
    # scenario_func = scenario_n_1  # !
    scenario_func = scenario_n_2
    # scenario_func = scenario_n_3
    # scenario_func = scenario_n_4
    # scenario_func = scenario_n_5
    # scenario_func = scenario_n_6
    print(scenario_func.__name__)


    all_agents = scenario_func()
    init_message_boxes(all_agents, S_ITERATIONS)
    collisions = []
    for iteration in range(S_ITERATIONS):
        send_messages(all_agents, iteration)
        print_table_of_messages(all_agents, iteration)
        choices = print_and_return_choices(all_agents, iteration, True)
        collisions.append(choices)

    plot_results(all_agents, collisions)


if __name__ == '__main__':
    main()
