from hypothesis import given

from eulerian_graph import transform
from eulerian_graph.edge import Edge

from eulerian_graph.walk import *
from eulerian_graph.graph import Graph
from conf_test import EDGES, EDGE, NODE, NODES


@given(edges=EDGES)
def test_recursive_walk_returns(edges):
    G = Graph()
    G.add_edges_from(edges)
    G = transform.eulerify(G)
    assert recursive_walk(G)


@given(edges=EDGES)
def test_eulerian_graph_starting_point(edges):
    G: Graph = Graph()
    G.add_edges_from(edges)
    G = transform.eulerify(G)

    odd_nodes_count = len(
        [node for node in G.nodes if G.order(node) % 2]
    )
    w = recursive_walk(G)
    assert len(w) - 1 == len(G.edges)
    if odd_nodes_count == 2:
        assert w[0] != w[-1]
    elif odd_nodes_count == 0:
        assert w[0] == w[-1]
    else:
        assert False


@given(edges=EDGES)
def test_non_eulerian_graph_starting_point(edges):
    G = Graph()
    G.add_edges_from(edges)
    if not G.is_eulerian():
        w = recursive_walk(G)
        assert not w


def test_recursive_walk_with_a_dummy_graph():
    G = Graph()
    G.add_node(0)
    assert recursive_walk(G) == [0]


def test_recursive_walk_with_a_dummy_cyclic_graph():
    G = Graph()
    G.add_edges_from([(0, 1), (0, 1)])
    assert recursive_walk(G, node=0) == [0, 1, 0]


def test_recursive_walk_with_a_simple_cycle():
    G = Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
    w = recursive_walk(G, node=1)
    assert w == [1, 2, 3, 4, 1] or w == [1, 4, 3, 2, 1]


def test_recursive_walk_with_a_simple_odd_graph():
    G = Graph()
    edges = [(1, 2), (1, 2), (2, 3), (3, 1)]
    G.add_edges_from(edges)
    w = recursive_walk(G, node=2)
    assert w[-1] == 1


@given(edges=EDGES)
def test_recursive_walk(edges):
    G = Graph()
    G.add_edges_from(edges)

    if not G.is_eulerian():
        assert recursive_walk(G) == []

    G = transform.eulerify(G)
    w = recursive_walk(G)
    for u, v in zip(w[:-1], w[1:]):
        # It's possible to go from u to v
        assert Edge(u, v) in G.edges
        # Once done we drop the edge
        G.remove_edge(u, v)
    assert not G.edges
