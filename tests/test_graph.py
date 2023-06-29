import random
import pytest
from hypothesis import given
from eulerian_graph.edge import Edge

from eulerian_graph.graph import *
from conf_test import EDGES, EDGE, NODE, NODES


@pytest.fixture
def G():
    return Graph()


@given(edges=EDGES)
def test_graph(edges):
    G = Graph()
    assert not len(G)
    G.add_edges_from(edges)
    assert len(G) >= 1


@given(u=NODE)
def test_add_node(u: int):
    G = Graph()
    G.add_node(u)
    assert u in G.nodes


@given(e=EDGE)
def test_add_edge(e):
    G = Graph()
    assert G.edges == []
    u, v = e
    G.add_edge(u, v)
    assert Edge(u, v) in G.edges


@given(nodes=NODES)
def test_add_nodes_from(nodes):
    G = Graph()
    G.add_nodes_from(nodes)
    assert G.nodes == nodes


@given(edges=EDGES)
def test_add_edges_from(edges):
    G = Graph()
    G.add_edges_from(edges)

    # Build Edge from tuple
    edges = [Edge(u, v) for u, v in edges]
    assert G.edges == edges


@given(u=NODE, edges=EDGES)
def test_get_edges(u, edges):
    G = Graph()
    assert G.get_edges(u) == []
    G.add_edges_from(edges)
    if u in G.nodes:
        assert G.get_edges(u)


@given(u=NODE, edges=EDGES)
def test_remove_node(u, edges):
    G = Graph()
    G.add_edges_from(edges)
    if u in G.nodes:
        G.remove_node(u)
        assert not G.get_edges(u)


def test_remove_tricky_node():
    G = Graph()
    edges = [(0, 0), (0, 0), (1, 1)]
    G.add_edges_from(edges)

    G.remove_node(0)
    assert G.edges == [Edge(1, 1)]


def test_order():
    G = Graph()
    G.add_edges_from(
        [(1, 2), (2, 1), (2, 3), (4, 4)]
    )
    assert G.order(1) == 2
    assert G.order(3) == 1
    assert G.order(4) == 2


def test_koenigsberg_is_not_eulerian():
    G = Graph()
    edges = [{1, 2}, {1, 2}, {1, 3}, {1, 4}, {1, 4}, {2, 3}, {3, 4}]
    G.add_edges_from(edges)
    assert not G.is_eulerian()
    u, v = random.sample(edges, k=1)[0]
    G.add_edge(u, v)
    assert G.is_eulerian()
