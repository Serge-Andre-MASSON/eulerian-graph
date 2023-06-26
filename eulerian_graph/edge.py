from typing import NamedTuple


class Edge(NamedTuple):
    """Model an undirected edge."""
    u: int
    v: int

    def __eq__(self, e: "Edge"):
        u, v = self.u, self.v
        return (u, v) == (e.u, e.v) or (u, v) == (e.v, e.u)
