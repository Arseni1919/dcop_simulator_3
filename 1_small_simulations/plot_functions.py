from functions import *


def plot_collisions(all_agents, collisions):
    robots = list(filter(lambda x: 'rob' in x.name, all_agents))
    position_objects = list(filter(lambda x: 'pos' in x.name, all_agents))
    robot_dict = {x.name: x.num for x in robots}
    position_dict = {x.name: x.num for x in position_objects}

    plot_dict = {x.name: [] for x in robots}
    for iteration, robot_name_to_pos_dict in enumerate(collisions):
        for robot_name, positions in robot_name_to_pos_dict.items():
            plot_dict[robot_name].extend([position_dict[x] for x in positions])

    for name, positions in plot_dict.items():
        plt.plot(list(range(len(positions))), positions, label=name)

    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Positions')
    plt.yticks([x.num for x in position_objects])
    plt.show()


def plot_results(all_agents, collisions):
    plot_collisions(all_agents, collisions)






