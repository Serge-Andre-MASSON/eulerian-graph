from inspect import getsource
import streamlit as st

import streamlit as st
from eulerian_graph.edge import Edge
from eulerian_graph.graph import Graph

from eulerian_graph.walk import recursive_walk, stack_walk


st.set_page_config(page_title="Les algorithmes")
st.sidebar.markdown("# Les septs ponts de Koenigsberg")


def modelisation():
    st.markdown("# Modélisation du graphe")
    networkx_url = "https://networkx.org/documentation/stable/index.html"
    st.write(
        f"""La modélisation présentée ici ainsi que son api est une version simplifiée de celle de la bibliothèque [networkx]({networkx_url}).""")

    st.markdown("## Arêtes et sommets")
    st.write(
        """Les sommets sont représentés par des entiers et une arête n'étant que la donnée de deux sommets d'un graphe on peut la modéliser par un tuple de deux entiers.""")

    st.write("""On surcharge la méthode __\_\_eq\_\___ pour que (u, v) = (v, u). Cela exprime le fait que les arêtes peuvent être aprcourues dans les deux sens.""")

    code = getsource(Edge)
    st.code(code)

    st.markdown("## Graphe")
    st.write("""On modélise le graphe de la façon suivante""")

    code = getsource(Graph)
    st.code(code)


def recursive():
    st.markdown("""## Algorithme de Hierholzer""")

    st.write("""L'implémentation proposée ici est une réécriture de la méthode proposée par Carl Hierholzer pour prouver l'existence d'une chaine dans un graphe donné. Une version optimisée est proposée dans la section suivante.""")

    st.write("""Dans le cas où le graphe n'a aucun sommet impair on commence par choisir un sommet au hasard et on trace un chemin à partir de celui-ci. Puisque tous les sommets rencontrés en chemin sont d'ordre pair, le seul sommet sur lequel on peut être bloqué est le sommet de départ.""")
    st.write(
        """On obtient alors un cycle """)
    st.latex(r"""u_0,\ u_1,\ u_2,\ \text{ ... } u_n, u_0""")
    st.write(
        """Si toutes les arêtes ont été utilisées alors c'est fini. Sinon on repart de n'importe quel sommet $v_0 = u_i$ du chemin déjà tracé ayant encore des arếtes, ce qui permet d'obtenir un nouveau cycle $v_0,\\ v_1,\\ v_2,\\ \\text{ ... } v_m, v_0$ que l'on peut insérer dans le cycle précédent en lieu et place du sommet qui avait encore des arêtes :""")
    st.latex(
        r"""u_0,\ u_1,\ u_2,\ \text{ ... } u_{i-1}, v_0,\ v_1,\ \text{ ... } v_m, v_0, u_{i+1} \text{ ... } u_n, u_0""")

    st.write("""On réitère alors le processus autant de fois que nécéssaire.""")

    st.write("""Lorsque le graphe à deux sommets d'ordre impair, on choisit l'un de ces deux sommets comme point de départ et on trace un chemin à partir de celui-ci. Le seul sommet sur lequel on peut rester bloqué est l'autre sommet impair. Lorsque cela arrive, on note que les arêtes restantes (non utilisées) forment un graphe dans lequel tous les sommets sont d'ordre pair. On est donc ramené au cas précédent et on applique la même procédure à partir d'un sommet du chemin déjà tracé.""")

    code = getsource(recursive_walk)
    st.code(code)


def stack():
    st.markdown("""## Algorithme de Hierholzer optimisé""")
    st.write("""Cette implémntation suivante repose sur l'utilisation d'une pîle. Les raîsons pour lesquelles cette algorithme fonctionne sont les mêmes que celles évoquées dans la section précédente.""")

    code = getsource(stack_walk)
    st.code(code)


page_names_to_funcs = {
    "Modélisation du graphe": modelisation,
    "Algorithme basique": recursive,
    "Algorithme optimisé": stack
}

selected_page = st.sidebar.selectbox(
    "Algorithme", page_names_to_funcs.keys(), label_visibility="hidden")

page_names_to_funcs[selected_page]()
