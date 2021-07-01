from nodes import *
from scenarios import *
from processes import *
from plot_functions import *


def main():
    print('Hello')
    # scenario_func = scenario_n_1  # !
    # scenario_func = scenario_n_2
    # scenario_func = scenario_n_3
    scenario_func = scenario_n_4

    all_agents = scenario_func()
    init_message_boxes(all_agents, ITERATIONS)
    collisions = []
    for iteration in range(ITERATIONS):
        send_messages(all_agents, iteration)
        print_table_of_messages(all_agents, iteration)
        choices = print_and_return_choices(all_agents, iteration)
        collisions.append(choices)

    plot_results(all_agents, collisions)


if __name__ == '__main__':
    main()
