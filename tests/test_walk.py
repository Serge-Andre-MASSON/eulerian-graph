from hypothesis import given
import pytest

from eulerian_graph import transform
from eulerian_graph.edge import Edge

from eulerian_graph.walk import *
from eulerian_graph.graph import Graph
from conf_test import EDGES


class Method(Enum):
    RECURSIVE = recursive_walk
    STACK = stack_walk


WALKS = [Method.RECURSIVE, Method.STACK]


@pytest.mark.parametrize('walk', WALKS)
@given(edges=EDGES)
def test_walk_returns(edges, walk):
    G = Graph()
    G.add_edges_from(edges)
    G = transform.eulerify(G)
    assert walk(G)


@pytest.mark.parametrize('walk', WALKS)
@given(edges=EDGES)
def test_eulerian_graph_starting_point(edges, walk):
    G: Graph = Graph()
    G.add_edges_from(edges)
    G = transform.eulerify(G)

    odd_nodes_count = len(
        [node for node in G.nodes if G.order(node) % 2]
    )
    w = walk(G)
    assert len(w) - 1 == len(G.edges)
    if odd_nodes_count == 2:
        assert w[0] != w[-1]
    elif odd_nodes_count == 0:
        assert w[0] == w[-1]
    else:
        assert False


@pytest.mark.parametrize('walk', WALKS)
@given(edges=EDGES)
def test_non_eulerian_graph(edges, walk):
    G = Graph()
    G.add_edges_from(edges)
    if not G.is_eulerian():
        w = walk(G)
        assert not w


@pytest.mark.parametrize('walk', WALKS)
def test_walk_with_a_dummy_graph(walk):
    G = Graph()
    G.add_node(0)
    assert walk(G) == [0]


@pytest.mark.parametrize('walk', WALKS)
def test_walk_with_a_dummy_cyclic_graph(walk):
    G = Graph()
    G.add_edges_from([(0, 1), (0, 1)])
    assert walk(G, node=0) == [0, 1, 0]


@pytest.mark.parametrize('walk', WALKS)
def test_recursive_walk_with_a_simple_cycle(walk):
    G = Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
    w = walk(G, node=1)
    assert w == [1, 2, 3, 4, 1] or w == [1, 4, 3, 2, 1]


@pytest.mark.parametrize('walk', WALKS)
def test_recursive_walk_with_a_simple_odd_graph(walk):
    G = Graph()
    edges = [(1, 2), (1, 2), (2, 3), (3, 1)]

    G.add_edges_from(edges)
    w = walk(G, node=1)
    assert w[-1] == 2
    w = walk(G, node=2)
    assert w[-1] == 1


@pytest.mark.parametrize('walk', WALKS)
def test_recursive_walk_with_an_odd_graph(walk):
    G = Graph()
    edges = [
        (1, 2),
        (2, 3), (3, 4), (4, 2),
        (2, 5), (5, 6),
        (6, 7), (7, 8), (8, 6),
        (6, 9)
    ]
    G.add_edges_from(edges)
    w = walk(G, node=1)
    assert w[-1] == 9
    w = walk(G, node=9)
    assert w[-1] == 1


@pytest.mark.parametrize('walk', WALKS)
@given(edges=EDGES)
def test_walk(edges, walk):
    G = Graph()
    G.add_edges_from(edges)

    if not G.is_eulerian():
        assert walk(G) == []

    G = transform.eulerify(G)
    w = walk(G)
    for u, v in zip(w[:-1], w[1:]):
        # It's possible to go from u to v
        assert Edge(u, v) in G.edges
        # Once done we drop the edge
        G.remove_edge(u, v)
    assert not G.edges
