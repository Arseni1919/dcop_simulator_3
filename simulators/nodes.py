from simulators.functions import *

class Node(abc.ABC):
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.neighbours = []
        # iteration -> name -> position -> value
        self.message_box = {}
        # --- for big sim --- #
        self.initial_pos_node = None
        self.delay = 0

        if str(num) not in name:
            raise RuntimeError('num is not in name')

    @abc.abstractmethod
    def send_message_to(self, nei, iteration):
        pass

    def clean_neighbours(self):
        self.neighbours = []


class FunctionNode(Node):
    def __init__(self, name, num):
        super().__init__(name, num)

    @abc.abstractmethod
    def comb_for_func(self, var_nei, pos_i, comb_of_other_nei_pos, list_of_other_nei):
        pass

    @abc.abstractmethod
    def func(self, comb):
        pass

    def _create_list_of_domains(self, send_to_var_nei):
        list_of_other_domains = []
        list_of_other_nei = []
        for nei in self.neighbours:
            if nei.name != send_to_var_nei.name:
                list_of_other_domains.append(nei.domain)
                list_of_other_nei.append(nei)
        return list_of_other_domains, list_of_other_nei

    def _prev_iter_brings(self, iteration, comb_of_other_nei_pos, list_of_other_nei):
        if iteration == 0:
            return 0
        prev_iteration_brings = 0
        for other_nei_pos, other_nei in zip(comb_of_other_nei_pos, list_of_other_nei):
            # iteration -> name -> position -> value
            prev_iteration_brings += self.message_box[iteration - 1][other_nei.name][other_nei_pos]
        return prev_iteration_brings

    def send_message_to(self, var_nei, iteration):
        message = {pos_i: MINUS_INF for pos_i in var_nei.domain}
        list_of_other_domains, list_of_other_nei = self._create_list_of_domains(var_nei)
        comb_of_other_nei_pos_list = list(itertools.product(*list_of_other_domains))
        # print(f"\r {self.name}'s len of comb_of_other_nei_pos_list: {len(comb_of_other_nei_pos_list)} ...", end='')
        for comb_of_other_nei_pos in comb_of_other_nei_pos_list:
            for pos_i in var_nei.domain:
                message[pos_i] = max(message[pos_i],
                                     (
                                             self.func(self.comb_for_func(var_nei, pos_i, comb_of_other_nei_pos,
                                                                          list_of_other_nei)
                                                       ) +
                                             self._prev_iter_brings(iteration, comb_of_other_nei_pos, list_of_other_nei)
                                     )
                                     )
        # if self.name == 'pos1' and var_nei.name == 'robot1':
        #     print(f'message from {self.name} to {var_nei.name} is: {message}')
        message = flatten_message(message)
        var_nei.message_box[iteration][self.name] = message


class TargetNode(FunctionNode):
    def __init__(self, name, num, req: int, cells_near_me: list):
        super().__init__(name, num)
        self.req = req
        self.cells_near_me = cells_near_me

        if 'target' not in name:
            raise RuntimeError('target is not in name')

    def comb_for_func(self, var_nei, pos_i, comb_of_other_nei_pos, list_of_other_nei):
        # comb = {"name_of_nei": binary(0,1), ... } | 1 - in, 0 - out
        comb = {var_nei.name: int(pos_i in self.cells_near_me)}
        for other_nei_pos, other_nei in zip(comb_of_other_nei_pos, list_of_other_nei):
            comb[other_nei.name] = int(other_nei_pos in self.cells_near_me)
        return comb

    def func(self, comb):
        # comb = {"name_of_nei": binary(0,1), ... } | 1 - in, 0 - out
        coverage = 0
        for var_nei_name, under_cov in comb.items():
            var_nei = list(filter(lambda x: x.name == var_nei_name, self.neighbours))[0]
            coverage += var_nei.cred if under_cov else 0
        return min(coverage, self.req)


class PositionNode(FunctionNode):
    def __init__(self, name, num, dict_of_weights: dict):
        super().__init__(name, num)
        self.dict_of_weights = dict_of_weights

        if 'pos' not in name:
            raise RuntimeError('pos is not in name')

    def comb_for_func(self, var_nei, pos_i, comb_of_other_nei_pos, list_of_other_nei):
        # comb = {"name_of_nei": binary(0,1), ... } | 1 - in, 0 - out
        comb = {var_nei.name: int(pos_i in [self.name, self.num])}
        for other_nei_pos, other_nei in zip(comb_of_other_nei_pos, list_of_other_nei):
            comb[other_nei.name] = int(other_nei_pos in [self.name, self.num])
        return comb

    def func(self, comb):
        # comb = {"name_of_nei": binary(0,1), ... } | 1 - in, 0 - out
        if sum(comb.values()) > 1:
            return MINUS_INF
        if sum(comb.values()) == 0:
            return 0
        name_of_nei = list(comb.keys())[list(comb.values()).index(1)]
        return self.dict_of_weights[name_of_nei]


class RobotNode(Node):
    def __init__(self, name, num, cred: int, domain: list):
        super().__init__(name, num)
        self.cred = cred
        self.domain = domain

        if 'robot' not in name:
            raise RuntimeError('robot is not in name')

    def send_message_to(self, func_nei, iteration):
        message = {pos_i: 0 for pos_i in self.domain}

        if iteration > 0:
            for nei in self.neighbours:
                if nei.name != func_nei.name:
                    past_message = self.message_box[iteration - 1][nei.name]
                    for d in self.domain:
                        message[d] += past_message[d]

        message = flatten_message(message)
        func_nei.message_box[iteration][self.name] = message


class BigSimulationPositionNode(PositionNode):
    def __init__(self, name, num, dict_of_weights: dict, pos: tuple):
        super().__init__(name, num, dict_of_weights)
        self.nearby_position_nodes = {}
        self.pos = pos

    def update_dict_of_weights(self, robots):
        self.dict_of_weights = create_dict_of_weights(robots)


class BigSimulationTargetNode(TargetNode):
    def __init__(self, name, num, req: int, cells_near_me=None, pos_node: BigSimulationPositionNode = None):
        super().__init__(name, num, req, cells_near_me)
        if cells_near_me is None:
            self.cells_near_me = []
        self.pos_node = pos_node
        self.fmr_set = []

    def update_cells_near_me(self, robots, graph):
        cells_near_me = []
        pos_dict = {pos.name: pos for pos in graph}
        for robot in robots:
            for nearby_pos_node_name in robot.domain:
                nearby_pos_node = pos_dict[nearby_pos_node_name]
                if distance(self.pos_node.pos, nearby_pos_node.pos) < robot.sr:
                    cells_near_me.append(nearby_pos_node_name)

        self.cells_near_me = list(set(cells_near_me))

    def clean_neighbours(self):
        self.neighbours = []
        self.fmr_set = []

    def clear_cells_near_me(self):
        self.cells_near_me = []


class BigSimulationRobotNode(RobotNode):
    def __init__(self, name, num, cred: int, domain=None, pos_node: BigSimulationPositionNode = None):
        super().__init__(name, num, cred, domain)
        # if domain is None:
        #     domain = []
        # self.domain = domain
        self.pos_node = pos_node
        self.prev_pos_node = None
        self.next_pos_node = None
        self.breakdown_pose = None
        self.breakdowns = False
        self.sr = SR
        self.mr = MR

    def update_domain(self):
        self.domain = [node.name for node in self.pos_node.nearby_position_nodes.values()]
        self.domain.insert(0, self.pos_node.name)

    def reset(self):
        self.pos_node = self.initial_pos_node
        self.prev_pos_node = None
        self.next_pos_node = None
        self.breakdown_pose = None
        self.delay = 0
        self.breakdowns = False

