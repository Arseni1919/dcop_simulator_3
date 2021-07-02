from functions import *


def plot_position_choices(all_agents, collisions):
    robots = list(filter(lambda x: 'rob' in x.name, all_agents))
    plot_dict_y = {x.name: [] for x in robots}
    plot_dict_x = {x.name: [] for x in robots}

    position_objects = list(filter(lambda x: 'pos' in x.name, all_agents))
    position_dict = {x.name: x.num for x in position_objects}

    for iteration, robot_name_to_pos_dict in enumerate(collisions):
        for robot_name, position_names in robot_name_to_pos_dict.items():
            plot_dict_y[robot_name].extend([position_dict[x] for x in position_names])
            plot_dict_x[robot_name].extend([iteration for _ in position_names])

    for robot_name, position_nums in plot_dict_y.items():
        plt.plot(plot_dict_x[robot_name], position_nums, 'o-', label=robot_name, alpha=0.5)

    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Positions')
    plt.yticks([x.num for x in position_objects])
    plt.xticks(list(range(len(collisions))))
    plt.show()


def plot_results(all_agents, collisions):
    plot_position_choices(all_agents, collisions)






