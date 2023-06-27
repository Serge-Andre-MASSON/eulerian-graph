from matplotlib import pyplot as plt
import networkx as nx


def draw(G_, ax=None, seed=7):
    G = nx.MultiGraph()
    G.add_edges_from(G_.edges)
    G.add_nodes_from(G_.nodes)
    layout = nx.spring_layout(G, seed=seed)
    if ax is None:
        ax = plt.subplot()

    nx.draw_networkx_nodes(G, layout, ax=ax)
    nx.draw_networkx_labels(G, layout, ax=ax)

    plotted_edges = []
    edge_multiplicities = get_edges_multiplicity(G)
    for edge in G.edges:
        if edge[:-1] in plotted_edges:
            continue
        multiplicity = edge_multiplicities[edge[:-1]]

        for i in range(multiplicity):
            arc_rad = (-1)**i * \
                i * .25 if multiplicity % 2 else (-1)**(i)*(i+1) * .25
            nx.draw_networkx_edges(
                G, layout, [edge],
                connectionstyle=f'arc3, rad = {arc_rad}',
                arrows=True,
                ax=ax)


def get_edges_multiplicity(G: nx.MultiGraph):
    multiplicity_dict = {}
    for edge in G.edges:
        u, v, _ = edge
        if (u, v) in multiplicity_dict:
            multiplicity_dict[(u, v)] += 1
        else:
            multiplicity_dict[(u, v)] = 1
    return multiplicity_dict
