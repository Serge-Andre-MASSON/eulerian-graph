from eulerian_graph.edge import Edge


def test_edge_equal_reversed_edge():
    e_1 = Edge(2, 4)
    e_2 = Edge(4, 2)
    assert e_1 == e_2
