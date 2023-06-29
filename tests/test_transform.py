from hypothesis import given

from eulerian_graph.graph import Graph
from eulerian_graph.transform import *
from eulerian_graph.transform import _is_connexe
from conf_test import EDGES


@given(edges=EDGES)
def test_connexify_graph(edges):
    G = Graph()
    G.add_edges_from(edges)

    G = connexify(G)
    connexe = is_connexe(G)
    assert connexe


@given(edges=EDGES)
def test_eulerian_graph_without_odd_nodes(edges):
    G: Graph = Graph()
    G.add_edges_from(edges)
    G = eulerify(G, 0)
    assert is_connexe(G)
    assert len(G) >= 1
    assert G._odd_nodes_count() == 0


@given(edges=EDGES)
def test_eulerian_graph_with_two_odd_nodes(edges):
    G: Graph = Graph()
    G.add_edges_from(edges)
    G = eulerify(G, 2)
    assert is_connexe(G)
    assert len(G) >= 1
    assert G._odd_nodes_count() <= 2


def test_is_connexe():
    C = Graph()
    C_is_connexe, visited_nodes = _is_connexe(C)
    assert not C_is_connexe
    assert not visited_nodes

    C.add_edges_from(
        [(1, 2), (2, 3), (3, 4)]
    )
    C_is_connexe, visited_nodes = _is_connexe(C)
    assert C_is_connexe
    assert set(visited_nodes) == set(C.nodes)

    C.add_edge(5, 6)
    C_is_connexe, visited_nodes = _is_connexe(C)
    assert not C_is_connexe

    assert visited_nodes == {5, 6} or visited_nodes == {1, 2, 3, 4}
