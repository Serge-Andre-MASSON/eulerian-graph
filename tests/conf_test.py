from hypothesis import strategies as st


NODE = st.integers(0, 15)
NODES = st.sets(NODE, min_size=1, max_size=25)
EDGE = st.tuples(NODE, NODE)

EDGES = st.lists(EDGE, min_size=1, max_size=25)
