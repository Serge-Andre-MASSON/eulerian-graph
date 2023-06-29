from typing import Iterable

from eulerian_graph.edge import Edge


class Graph:
    """Model an undirected multi edges graph."""

    def __init__(self):
        """A multi edges graph is defined by its nodes and (undirected) edges. Nodes are uniques but edges can be duplicated."""
        self.nodes: set[int] = set()
        self.edges: list[Edge] = list()
        self.orders: dict = dict()

    def __len__(self):
        return len(self.nodes)

    def add_node(self, v: int):
        """Add the node v if it's not already in the graph."""
        self.nodes.add(v)

    def add_nodes_from(self, nodes: list[int]):
        """Add nodes to the graph. Do nothing if a node is already in the graph."""
        for node in nodes:
            self.add_node(node)

    def add_edge(self, u, v):
        """Add an edge between u and v in the graph. Nodes u and v are created if necessary."""
        self.add_nodes_from([u, v])
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
        edges_to_remove = self.get_edges(u)
        for edge in edges_to_remove:
            self.remove_edge(*edge)
        self.nodes.remove(u)

    def get_edges(self, u: int = None):
        """return all edges or ,ust the ones coming from node u if specified."""
        if u is None:
            return self.edges
        return [edge for edge in self.edges if u in edge]

    def order(self, u: int):
        """Return the order of u"""
        order = 0
        for edge in self.get_edges(u):
            order += edge.count(u)
        return order

    def _odd_nodes_count(self):
        odd_nodes = self._odd_nodes()
        return len(odd_nodes)

    def _odd_nodes(self):
        return [node for node in self.nodes if self.order(node) % 2]

    def is_eulerian(self):
        """Return True if the graph has a path or a cycle, False otherwise."""
        return self._odd_nodes_count() in [0, 2]
