from simulators.plots.plot_functions import *


def send_messages(agents, iteration):
    for agent in agents:
        # print(agent.name)
        for nei in agent.neighbours:
            agent.send_message_to(nei, iteration)


def plot_results(all_agents, collisions):
    plot_position_choices(all_agents, collisions)











