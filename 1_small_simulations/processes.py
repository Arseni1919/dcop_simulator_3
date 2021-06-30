from functions import *


def send_messages(agents, iteration):
    for agent in agents:
        # print(agent.name)
        for nei in agent.neighbours:
            agent.send_message_to(nei, iteration)


def init_message_boxes(agents, iterations):
    for agent in agents:
        for itr in range(iterations):
            agent.message_box[itr] = {}
            for nei in agent.neighbours:
                agent.message_box[itr][nei.name] = {}


def print_table_of_messages(all_agents, iteration):
    headers = ["to \ from", ]
    for a in all_agents:
        headers.append(a.name)
    table = PrettyTable(headers)
    for a in all_agents:
        raw = [a.name]
        for b in all_agents:
            if b.name in a.message_box[iteration]:
                cell_to_print = ''
                for k, v in a.message_box[iteration][b.name].items():
                    cell_to_print = cell_to_print + str(k) + '->' + str(round(v, 2)) + '\n'
                raw.append(cell_to_print)
            else:
                raw.append('')
        table.add_row(raw)

    print('---')
    print(colored('### ITERATION: %s ###', 'yellow', 'on_grey') % (iteration + 1))
    print(table)


def print_choices(all_agents, iteration):
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
            print(colored(a.name, 'green'), end=' ')
            choose_str = 'chooses one of' if len(cells_with_highest_value) > 1 else 'chooses'
            print(f'{choose_str}: {cells_with_highest_value}', end=' ')
            print(f'with the highest value: {max_value:.2f}')
            assignments.extend(cells_with_highest_value)
    # print_all_pos_sum_weights(all_agents, iteration)
    return len(assignments) > len(set(assignments))






