from nodes import *
from scenarios import *
from processes import *


def main():
    print('Hello')
    scenario_func = scenario_n_1  # !
    scenario_func = scenario_n_2

    all_agents = scenario_func()
    init_message_boxes(all_agents, ITERATIONS)
    collisions = []
    for iteration in range(ITERATIONS):
        send_messages(all_agents, iteration)
        print_table_of_messages(all_agents, iteration)
        print_choices(all_agents, iteration)
        # collisions.append(print_choices(all_agents, iteration))


if __name__ == '__main__':
    main()
