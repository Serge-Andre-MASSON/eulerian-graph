from collections import deque
from copy import deepcopy
import random
from eulerian_graph.graph import Graph


def connexify(G: Graph):
    G_is_connexe, visited_nodes = _is_connexe(G)
    if G_is_connexe:
        return G
    C = deepcopy(G)
    for node in G.nodes - visited_nodes:
        C.remove_node(node)
    return C


def _is_connexe(G: Graph, return_visited_nodes=True):
    if not len(G):
        if return_visited_nodes:
            return False, set()
        else:
            return False

    node = random.choice(list(G.nodes))  # set is not choice able...
    visited_nodes = set()
    nodes_to_visit = deque([node])

    while nodes_to_visit:
        current_node = nodes_to_visit.popleft()
        visited_nodes.add(current_node)
        for edge in G.get_edges(current_node):
            node = edge.u if current_node == edge.v else edge.v
            if node not in visited_nodes:  # change here to node to visit
                nodes_to_visit.append(node)
    if return_visited_nodes:
        return G.nodes == visited_nodes, visited_nodes
    else:
        return G.nodes == visited_nodes


def is_connexe(G: Graph):
    return _is_connexe(G, return_visited_nodes=False)


def eulerify(G: Graph, max_odd_nodes_count: int = 2):
    G: Graph = connexify(G)
    if G._odd_nodes_count() <= max_odd_nodes_count:
        return G

    while G._odd_nodes_count() > max_odd_nodes_count:
        odd_nodes = [node for node in G.nodes if G.order(node) % 2]
        u, v = random.sample(odd_nodes, k=2)
        G.add_edge(u, v)
    return G
