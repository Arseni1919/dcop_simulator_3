import random

from simulators.functions import *


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


def select_pos_old(pos_set, temp_req_set, robot):
    """
    input:
    pos_set = [(x1, y1),(x2, y2),..]
    targets = [(target, temp_req), (target, temp_req), ..]
    SR = int()
    output:
    pos = (x, y)
    """
    if len(pos_set) == 1:
        return pos_set[0]
    target_set = get_target_set_with_SR_range(pos_set, temp_req_set, robot.sr)
    if len(target_set) == 0:
        return random.choice(pos_set)
    # target_set changes if not all targets can fit
    possible_pos, new_target_set = get_possible_pos(pos_set, target_set, robot.sr)
    new_temp_req_set = get_new_targets(target_set, temp_req_set)
    return select_pos_old(possible_pos, new_temp_req_set, robot)


def get_target_set_with_SR_range(pos_set, temp_req_set, sr):
    """

    input:
    output:
    """
    target_set = []
    req_list_max_to_min = get_req_list_max_to_min(temp_req_set)
    for max_req in req_list_max_to_min:
        for target_tuple in temp_req_set:
            target, temp_req = target_tuple
            if temp_req == max_req:
                for pos in pos_set:
                    if distance(pos, target.pos_node.pos) < sr:
                        target_set.append(target_tuple)
        if len(target_set) > 0:
            return target_set
    return target_set


def get_req_list_max_to_min(targets):
    """
    input:
    output:
    """
    req_list_max_to_min = []
    for target_tuple in targets:
        _, temp_req = target_tuple
        req_list_max_to_min.append(temp_req)
    return_value = sorted(req_list_max_to_min)
    # return_value = sorted(list(req_list_max_to_min), reverse=True)
    return return_value


def get_possible_pos(pos_set, target_set, sr):
    """
    input:
    output:
    """
    best_value = 0
    new_target_set = []
    possible_pos = []
    for pos in pos_set:
        pos_cart = []
        for target_tuple in target_set:
            target, temp_req = target_tuple
            if distance(pos, target.pos_node.pos) < sr:
                pos_cart.append(target_tuple)
        if len(pos_cart) > best_value:
            best_value = len(pos_cart)
            new_target_set = pos_cart

    for pos in pos_set:
        good = True
        for target_tuple in new_target_set:
            target, temp_req = target_tuple
            if not distance(pos, target.pos_node.pos) < sr:
                good = False
                break
        if good:
            possible_pos.append(pos)

    return possible_pos, new_target_set


def get_new_targets(target_set, temp_req_set):
    """
    input:
    output:
    """
    new_temp_req_set = []
    for target, target_req in temp_req_set:
        if target not in target_set:
            new_temp_req_set.append((target, target_req))
    return new_temp_req_set







