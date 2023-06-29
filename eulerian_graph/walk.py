from copy import deepcopy
from enum import Enum
from random import choice
import random

from eulerian_graph.graph import Graph


def recursive_walk(G: Graph, node: int = None, path: list = []):
    if not G.is_eulerian():
        return []
    G = deepcopy(G)
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
        path = recursive_walk(G, node, path)

    return path


def stack_walk(G: Graph, node: int = None, path=None):
    if not G.is_eulerian():
        return []
    G = deepcopy(G)
    if node is None:
        node = get_starting_node(G)
    node_stack = [node]

    if path is None:
        path = []

    while node_stack:
        node = node_stack[-1]

        edges = G.get_edges(node)
        if edges:
            u, v = random.choice(edges)
            node = u if node == v else v
            node_stack.append(node)
            G.remove_edge(u, v)

        else:
            last_node = node_stack.pop()
            path.append(last_node)

    return path[::-1]


def get_starting_node(G: Graph):
    odd_nodes = [node for node in G.nodes if G.order(node) % 2]
    if odd_nodes:
        return choice(odd_nodes)
    return choice(list(G.nodes))


def get_an_other_node_with_edges(G: Graph, path):
    for node in path:
        if G.get_edges(node):
            return node


def insert_list(l, into, at):
    return into[:at] + l + into[at+1:]
