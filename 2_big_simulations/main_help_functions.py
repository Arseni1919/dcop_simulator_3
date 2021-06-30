from IMPORTS import *


def create_graph():
    graph = []

    x_list = [np.random.uniform(0, WIDTH) for _ in range(N_NODES)]
    y_list = [np.random.uniform(0, WIDTH) for _ in range(N_NODES)]

    xy = np.array(list(zip(x_list, y_list)))

    nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(xy)
    dists, indcs = nbrs.kneighbors(xy)

    plt.clf()
    plt.scatter(x_list, y_list)

    for node, indc_list in enumerate(indcs):
        self_cell = indc_list[0]
        n_nei = random.randint(3, 9)
        for j, nei in enumerate(indc_list[1:n_nei]):
            x_edges_list = []
            y_edges_list = []
            if dists[node][j + 1] < 50:
                x_edges_list.append(xy[self_cell][0])
                y_edges_list.append(xy[self_cell][1])

                x_edges_list.append(xy[nei][0])
                y_edges_list.append(xy[nei][1])

            plt.plot(x_edges_list, y_edges_list, alpha=0.5)
    plt.show()


    return graph














