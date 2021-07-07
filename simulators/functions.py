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
    if FLATTEN_MESSAGE:
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


def select_pos(robot, targets, graph):
    robot_pos_name_set = [pos_name for pos_name in robot.domain]
    pos_dict_name_pos = {pos_node.name: pos_node.pos for pos_node in graph}
    pos_dict_name_pos_node = {pos_node.name: pos_node for pos_node in graph}
    next_pos_name = select_pos_internal(robot, robot_pos_name_set, [t for t in targets], pos_dict_name_pos)
    return pos_dict_name_pos_node[next_pos_name]


def select_pos_internal(robot, robot_pos_name_set, funcs, pos_dict_name_pos):
    max_func_value = max([target.req for target in funcs])
    if len(robot_pos_name_set) == 1 or max_func_value < 1:
        return random.sample(robot_pos_name_set, 1)[0]
    target_set = []
    for target in funcs:
        if target.req == max_func_value:
            if any([distance(target.pos_node.pos, pos_dict_name_pos[p_n]) < robot.sr for p_n in robot_pos_name_set]):
                target_set.append(target)

    if len(target_set) == 0:
        return random.sample(robot_pos_name_set, 1)[0]

    within_sr_range_list, target_set = within_sr_from_most(robot, robot_pos_name_set, target_set, pos_dict_name_pos)
    for target in target_set:
        funcs.remove(target)

    return select_pos_internal(robot, within_sr_range_list, funcs, pos_dict_name_pos)


def within_sr_from_most(robot, robot_pos_name_set, target_set, pos_dict_name_pos):
    within_sr_range_dict = {}
    max_list = []
    for robot_name in robot_pos_name_set:
        count = sum([distance(target.pos_node.pos, pos_dict_name_pos[robot_name]) < robot.sr for target in target_set])
        max_list.append(count)
        within_sr_range_dict[robot_name] = count
    max_value = max(max_list)

    within_sr_range_list, target_set_to_send = [], []
    for robot_name, count in within_sr_range_dict.items():
        if count == max_value:
            within_sr_range_list.append(robot_name)
            target_set_to_send.extend(list(filter(
                lambda x: distance(x.pos_node.pos, pos_dict_name_pos[robot_name]) < robot.sr,
                target_set
            )))
    target_set_to_send = list(set(target_set_to_send))
    return within_sr_range_list, target_set_to_send


def breakdowns_correction(robots, params):
    if 'breakdowns' in params:
        for robot in robots[:]:
            if not robot.breakdowns:
                for nei_robot in robots[:]:
                    if robot.name != nei_robot.name and robot.pos_node is nei_robot.pos_node:
                        robot.breakdowns = True
                        robot.breakdown_pose = robot.pos_node
                        # print(f'\n{robot.name} and {nei_robot.name} in breakdown')
                        break
        for robot in robots[:]:
            if robot.breakdowns:
                # robots.remove(robot)
                robot.prev_pos_node = robot.breakdown_pose
                robot.pos_node = robot.breakdown_pose





































