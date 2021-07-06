import random

from simulators.constants_and_packages import *


def init_message_boxes(agents, iterations):
    for agent in agents:
        agent.message_box = {
            itr: {
                nei.name: {} for nei in agent.neighbours
            }
            for itr in range(iterations)
        }


def load_file(file_name):
    with open(file_name, 'rb') as fileObject:
        return pickle.load(fileObject)


def distance(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))


def calculate_coverage(robots, targets):
    convergence = 0
    for target in targets:
        curr_conv = target.req
        for robot in robots:
            if distance(target.pos_node.pos, robot.pos_node.pos) <= robot.sr:
                curr_conv = max(0, curr_conv - robot.cred)
        convergence += curr_conv
    return convergence


def calculate_collisions(robots, big_iteration):
    collisions = 0
    for robot1, robot2 in itertools.product(robots, robots):
        if robot1.name != robot2.name:
            if robot1.pos_node.num == robot2.pos_node.num:
                if big_iteration > 0 and robot1.prev_pos_node and robot1.prev_pos_node == robot1.pos_node:
                    continue
                collisions += 1
    return collisions


def print_minutes(start):
    end = time.time()
    print()
    print(f'\nThe program finished in {time.strftime("%H:%M:%S", time.gmtime(end - start))}.')


def flatten_message(message):
    if S_FLATTEN:
        min_value = min(message.values())
        return {pos_i: value - min_value for pos_i, value in message.items()}
    return message


def create_dict_of_weights(robots):
    # return_value = {robot.name: random.uniform(1e-3, 1e-1) for robot in robots}
    return_value = {robot.name: random.uniform(1e-10, 1e-5) for robot in robots}
    # return_value = {robot.name: 0 for robot in robots}
    return return_value


def print_and_return_choices(all_agents):
    # return_value: {'robot_name': ['pos_i', ...], 'robot_name_2': ['pos_i', ...], ...}
    return_value = {}
    str_for_print = ''

    for a in all_agents:
        s_iteration = len(list(a.message_box.keys())) - 1
        if 'robot' in a.name:
            counter_dict = {}
            for d in a.domain:
                counter_dict[d] = 0
            for b in all_agents:
                if b.name in a.message_box[s_iteration]:
                    for k, v in a.message_box[s_iteration][b.name].items():
                        counter_dict[k] += v

            max_value = max(counter_dict.values())
            cells_with_highest_value = [k for k, v in counter_dict.items() if v == max_value]
            choose_str = 'chooses one of' if len(cells_with_highest_value) > 1 else 'chooses'
            str_for_print += f'\n{colored(a.name, "green")} {choose_str}: ' \
                             f'{cells_with_highest_value} with the highest value: {max_value:.2f}'
            return_value[a.name] = cells_with_highest_value
    # print(str_for_print)
    # print_all_pos_sum_weights(all_agents, iteration)
    return return_value


def cover_target(target, robots_set):
    cumulative_cov = sum([robot.cred for robot in robots_set])
    return cumulative_cov > target.req


def select_FMR_nei(target):
    total_set = []
    SR_set = []
    rest_set = []

    for robot in target.neighbours:
        dist = distance(robot.pos_node.pos, target.pos_node.pos)

        if dist <= robot.sr + robot.mr:
            total_set.append(robot)
            if dist <= robot.sr:
                SR_set.append(robot)
            else:
                rest_set.append(robot)

    while cover_target(target, total_set):
        def get_degree(node):
            targets_nearby = list(filter(lambda x: 'target' in x.name, node.neighbours))
            return len(targets_nearby)
        max_degree = max([get_degree(x) for x in rest_set], default=0)
        min_degree = min([get_degree(x) for x in SR_set], default=0)
        if len(rest_set) > 0:
            selected_to_remove = list(filter(lambda x: get_degree(x) == max_degree, rest_set))[0]
            rest_set.remove(selected_to_remove)
        else:
            selected_to_remove = list(filter(lambda x: get_degree(x) == min_degree, SR_set))[0]
            SR_set.remove(selected_to_remove)

        temp_total_set = total_set[:]
        temp_total_set.remove(selected_to_remove)
        if not cover_target(target, temp_total_set):
            return total_set

        total_set.remove(selected_to_remove)
    return total_set


def set_diff_cred(robots, min_v, max_v):
    def set_cred(x):
        x.cred = random.randint(min_v, max_v)

    _ = [set_cred(x) for x in robots]




































