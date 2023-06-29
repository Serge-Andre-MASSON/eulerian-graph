from copy import deepcopy
from enum import Enum
from random import choice

from eulerian_graph.graph import Graph


def _recursive_walk(G: Graph, node: int = None, path: list = []):

    if node is None:
        node = get_starting_node(G)

    current_path = [node]

    edges = G.get_edges(node)
    while edges:
        u, v = choice(edges)
        G.remove_edge(u, v)
        node = u if node == v else v
        current_path.append(node)
        edges = G.get_edges(node)

    if not path:
        path = current_path
    else:
        index = path.index(node)
        path = insert_list(current_path, into=path, at=index)

    if G.get_edges():
        node = get_an_other_node_with_edges(G, path)
        path = _recursive_walk(G, node, path)

    return path


def recursive_walk(G: Graph, node: int = None, path=[]):
    if not G.is_eulerian():
        return []
    G = deepcopy(G)
    return _recursive_walk(G, node, path)


def stack_walk(G, start: int = None):
    pass


def get_starting_node(G: Graph):
    odd_nodes = [node for node in G.nodes if G.order(node) % 2]
    if odd_nodes:
        return choice(odd_nodes)
    return choice(list(G.nodes))


def get_an_other_node_with_edges(G: Graph, path):
    for node in path:
        if G.get_edges(node):
            return node


class Method(Enum):
    RECURSIVE = recursive_walk
    STACK = stack_walk


def walk(G, start: int = None, method: Method = Method.RECURSIVE):
    if method is Method.RECURSIVE:
        return recursive_walk(G, start)
    else:
        return stack_walk(G, start)


# def walk(G_: Graph, start=None, path=None, methode: str = "recursive"):
#     G = deepcopy(G_)  # Don't want to alter the original graph
#     odd_nodes = [node for node in G.nodes if G.get_node_order(node) % 2]
#     if len(odd_nodes) > 2:
#         return []

#     if start is None:
#         if odd_nodes:
#             start = choice(odd_nodes)
#         else:
#             start = choice(G.nodes)
#     if not path:
#         path = [start]
#     while True:

#         if not G.edges:
#             break

#         edges = G.get_edges_from_node(start)

#         if not edges:
#             G.remove_node(start)
#             for node in path[1:-1]:
#                 if G.get_edges_from_node(node):
#                     node_index = path.index(node)
#                     return insert_list(
#                         walk(G, start=node),
#                         into_list=path,
#                         at_index=node_index)
#             return path

#         edge = choice(edges)
#         G.remove_edge(*edge)

#         start = atomic_walk(start, edge)
#         path.append(start)

#     return path


def insert_list(l, into, at):
    return into[:at] + l + into[at+1:]
