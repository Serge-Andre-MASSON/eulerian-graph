from inspect import getsource

import streamlit as st

from eulerian_graph.edge import Edge


code = getsource(Edge)
st.code(code)
