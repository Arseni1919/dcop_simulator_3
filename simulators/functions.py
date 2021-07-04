import random

from simulators.constants_and_packages import *


def distance(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))


def calculate_convergence(robots, targets):
    convergence = 0
    for target in targets:
        curr_conv = target.req
        for robot in robots:
            if distance(target.pos_node.pos, robot.pos_node.pos) <= robot.sr:
                curr_conv = max(0, curr_conv - robot.cred)
        convergence += curr_conv
    return convergence


def update_domain(x):
    x.update_domain()
    return x


def init_message_box(x):
    x.message_box = {i: {} for i in range(B_ITERATIONS_IN_BIG_LOOPS)}


def print_minutes(start):
    end = time.time()
    print(f'\nThe program finished in {(end - start) / 60 :.2f} minutes.')


def flatten_message(message):
    if S_FLATTEN:
        min_value = min(message.values())
        return {pos_i: value-min_value for pos_i, value in message.items()}
    return message


def create_dict_of_weights(robots):
    # return_value = {robot.name: random.uniform(1e-3, 1e-1) for robot in robots}
    return_value = {robot.name: random.uniform(1e-10, 1e-5) for robot in robots}
    # return_value = {robot.name: 0 for robot in robots}
    return return_value


def print_and_return_choices(all_agents, iteration):
    # return_value: {'robot_name': ['pos_i', ...], 'robot_name_2': ['pos_i', ...], ...}
    return_value = {}
    assignments = []

    for a in all_agents:
        if 'robot' in a.name:
            counter_dict = {}
            for d in a.domain:
                counter_dict[d] = 0
            for b in all_agents:
                if b.name in a.message_box[iteration]:
                    for k, v in a.message_box[iteration][b.name].items():
                        counter_dict[k] += v

            max_value = max(counter_dict.values())
            cells_with_highest_value = [k for k, v in counter_dict.items() if v == max_value]
            choose_str = 'chooses one of' if len(cells_with_highest_value) > 1 else 'chooses'
            str_for_print = f'\n{colored(a.name, "green")} {choose_str}: ' \
                            f'{cells_with_highest_value} with the highest value: {max_value:.2f}'
            # print(str_for_print, end=' ')
            assignments.extend(cells_with_highest_value)
            return_value[a.name] = cells_with_highest_value
    # print_all_pos_sum_weights(all_agents, iteration)
    return return_value











