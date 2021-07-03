from simulators.functions import *


class Node(abc.ABC):
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.neighbours = []
        # iteration -> name -> position -> value
        self.message_box = {}

        if str(num) not in name:
            raise RuntimeError('num is not in name')

    @abc.abstractmethod
    def send_message_to(self, nei, iteration):
        pass


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

        for comb_of_other_nei_pos in comb_of_other_nei_pos_list:
            for pos_i in var_nei.domain:
                message[pos_i] = max(message[pos_i],
                                     (
                                         self.func(self.comb_for_func(var_nei, pos_i, comb_of_other_nei_pos, list_of_other_nei)
                                                   ) +
                                         self._prev_iter_brings(iteration, comb_of_other_nei_pos, list_of_other_nei)
                                     )
                                     )
        if self.name == 'pos1' and var_nei.name == 'robot1':
            print(f'message from {self.name} to {var_nei.name} is: {message}')
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


class BigSimulationTargetNode(TargetNode):
    def __init__(self, name, num, req: int, cells_near_me: [int], pos):
        super().__init__(name, num, req, cells_near_me)
        self.pos = pos


class BigSimulationRobotNode(RobotNode):
    def __init__(self, name, num, cred: int, domain: list, pos):
        super().__init__(name, num, cred, domain)
        self.pos = pos




