import random

from simulators.constants_and_packages import *


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
    assignments = []
    return_value = {}
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
            print(colored(a.name, 'green'), end=' ')
            choose_str = 'chooses one of' if len(cells_with_highest_value) > 1 else 'chooses'
            print(f'{choose_str}: {cells_with_highest_value}', end=' ')
            print(f'with the highest value: {max_value:.2f}')
            assignments.extend(cells_with_highest_value)
            return_value[a.name] = cells_with_highest_value
    # print_all_pos_sum_weights(all_agents, iteration)
    return return_value











