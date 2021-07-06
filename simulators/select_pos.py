from simulators.functions import *


def select_pos(pos_set, temp_req_set, robot):
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
    return select_pos(possible_pos, new_temp_req_set, robot.sr)


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
    return sorted(req_list_max_to_min, reverse=True)


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







