from simulators.constants_and_packages import *
from simulators.nodes import *
from simulators.plot_functions import *

def create_graph():
    graph = []
    x_list = [np.random.uniform(0, B_WIDTH) for _ in range(B_N_NODES)]
    y_list = [np.random.uniform(0, B_WIDTH) for _ in range(B_N_NODES)]
    xy = np.array(list(zip(x_list, y_list)))
    nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(xy)
    dists, indcs = nbrs.kneighbors(xy)

    for pos_indx, pos in enumerate(xy):
        graph.append(BigSimulationPositionNode(f'pos{pos_indx}', pos_indx, dict_of_weights={}, pos=pos))



    for node, indc_list in enumerate(indcs):
        self_pos = graph[indc_list[0]]
        n_nei = random.randint(3, 9)
        for j, nei in enumerate(indc_list[1:n_nei]):
            if dists[node][j + 1] < B_MAX_DISTANCE_OF_NEARBY_POS:
                nearby_pos = graph[nei]
                self_pos.nearby_position_nodes[nearby_pos.name] = nearby_pos

    return graph


def plot_results(graph):
    plot_positions_graph(graph)














