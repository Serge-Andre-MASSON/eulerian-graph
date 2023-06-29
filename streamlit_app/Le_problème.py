from eulerian_graph.draw import draw
from matplotlib import pyplot as plt
import streamlit as st

from eulerian_graph.graph import Graph


st.set_page_config(page_title="Le problème")

st.markdown("# Le problème")
st.write("""Jusqu'en 1735, les habitants de Koenigsberg se demandent s'il est possible de visiter leur ville en empruntant chacun de ses ponts une et une seule fois.""")
st.image("Konigsberg_bridges.png")
st.write("""C'est finalement Leonard Euler qui apporte la réponse, négative, à cette question. Son approche pour résoudre le problème commence avec une modélisation du problème sous forme d'un graphe où chaque sommet est une berge et chaque arête est un pont: """)


G = Graph()
edges = [{1, 2}, {1, 2}, {1, 3}, {1, 4}, {1, 4}, {2, 3}, {3, 4}]
G.add_edges_from(edges)

fig, ax = plt.subplots()
draw(G, ax=ax)
st.pyplot(fig)

st.write("""Ce qu'on l'on cherche s'appelle une "chaine eulérienne": un chemin le long des arêtes du graphe, les utilisant toutes une seule fois. Si ce chemin revient à son point de départ alors on parle de "cycle eulerien".""")

st.write("""Lorsqu'on parcourt un chemin sur un graphe et que l'on rencontre un sommet d'ordre $2n + 1$ (nombre d'arête(s) issue(s) du sommet), le seul moyen de parcourir une seule fois les $2n$ arêtes encore non utilisées est de faire $n$ aller-retour sur ce sommet jusqu'à s'y retrouver bloqué.""")
st.write("""On en déduit qu'un sommet d'ordre impair est soit le premier soit le dernier d'une chaîne. Il ne peut donc pas y en avoir plus que deux. Autrement dit""")
st.markdown(
    r"""$$ \text{G admet une chaîne eulerienne} \Rightarrow \text{G a au plus 2 sommets d'ordre impair} $$""")

st.write("""On peut réécrire cette condition sous la forme""")
st.markdown(
    r"""$$ \text{G admet une chaîne eulerienne} \Rightarrow \text{G a 0 ou 2 sommets d'ordre impair} $$""")
st.write("""en utilisant le fait qu'un graphe quelconque ne peut avoir qu'un nombre pair de sommet d'ordre impair, ce qui est du au fait que la somme des ordres de tous les sommet du graphe est nombre d'arête multiplié par deux.""")

st.write("""On peut aussi écrire une condition nécessaire pour l'existence d'un cycle :""")
st.markdown(
    r"""$$ \text{G admet un cycle eulerien} \Rightarrow \text{G n'a aucun sommets d'ordre impair} $$""")
st.write("""Pour s'en convaincre il suffit de voir qu'un cycle est un cas particulier de chaîne.""")

st.write("""S'il y a deux sommets d'ordre impair, les points de départ et d'arrivée sont distincts donc ce n'est pas un cycle. La seule possibilité restante est qu'il n'y en ait aucun.""")


st.write("""Le graphe modélisant le problème des ponts de Koenigsberg possédant quatre sommets d'ordre impair, il n'admet ni chaîne ni cycle et on ne peut donc pas visiter la ville en utilisant tous les ponts une seule fois.""")


# edges = ""
# edges = st.text_input('Add edges ("u_0,v_0 u_1, v_1 ...")')


# if edges:
#     for edge in edges.split():
#         u, v = [int(i) for i in edge.split(",")]
#         G.add_edge(u, v)

# G.draw(ax)
# st.pyplot(fig)
