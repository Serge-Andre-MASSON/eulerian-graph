from typing import Iterable

from eulerian_graph.edge import Edge


class Graph:
    """Model an undirected multi edge graph."""

    def __init__(self):
        """A graph is defined by its nodes and (undirected) edges. Nodes are uniques but edges can be duplicated."""
        self.nodes: list = list()
        self.edges: list[Edge] = list()

    def add_node(self, v: int):
        """Add the node v if it's not already in the graph."""
        if v not in self.nodes:
            self.nodes.append(v)

    def add_nodes_from(self, *nodes):
        """Add nodes to the graph. Do nothing if a node is already in the graph."""
        for node in nodes:
            self.add_node(node)

    def add_edge(self, u, v):
        """Add an edge between u and v in the graph. Nodes u and v are created if necessary."""
        self.add_nodes_from(u, v)
        edge = Edge(u, v)
        self.edges.append(edge)

    def add_edges_from(self, edges: list[Iterable | Edge]):
        """Add the list of edges to the graph."""
        for edge in edges:
            self.add_edge(*edge)

    def remove_edge(self, u, v):
        """Remove the edge. Do nothing if there is no such edge."""
        edge = Edge(u, v)
        try:
            self.edges.remove(edge)
        except ValueError:
            pass

    def remove_node(self, u):
        """Remove the specified node. If the node have edges, those are removed too."""
        try:
            self.nodes.remove(u)
            for edge in self.edges:
                if u in edge:
                    self.remove_edge(*edge)
        except ValueError:
            pass
