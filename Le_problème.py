from matplotlib import pyplot as plt
import streamlit as st


st.set_page_config(page_title="Le problème")
# st.sidebar.markdown("# Les septs ponts de Koenigsberg")

st.markdown("# Le problème")
st.write("""Jusqu'en 1735, les habitants de Koenigsberg se demandent s'il est possible de visiter la ville en empruntant chacun de ses ponts une et une seule fois.""")
st.image("Konigsberg_bridges.png")
st.write("""C'est finalement Leonard Euler qui apporte la réponse, négative, à cette question. Le succès de son approche pour résoudre le problème commence avec une modélisation du problème sous forme de graphe: """)


# G = Graph()
# edges = [{1, 2}, {1, 2}, {1, 3}, {1, 4}, {1, 4}, {2, 3}, {3, 4}]
# G.add_edges(edges)

# fig, ax = plt.subplots()
# G.draw(ax)
# st.pyplot(fig)

st.write("""Chaque sommet est une berge et chaque arête est un pont.""")

st.write("""Le nom mathématique de ce qu'on l'on cherche est une "chaine eulérienne": un chemin le long des arêtes du graphe, les utilisant toutes une seule fois.""")

st.write("""Pour la suite du raisonnement il faut définir la notion d'ordre d'un sommet : c'est le nombre d'arête(s) qui en sont issue(s).""")

st.write("""Supposons qu'il y ait une chaîne eulerienne dans ce graphe et essayons de la parcourir.""")
st.write("""De quelque sommet s0 que l'on vienne, le sommet s1 que l'on rencontre est d'ordre impair. On est donc dans une situation telle que celle ci""")
# G = Graph()
# G.add_edges([("s0", "s1"), ("s1", "s2"), ("s1", "s3")])
# fig, ax = plt.subplots()
# G.draw(ax)
# st.pyplot(fig)

st.write("""Quelque soit l'arête que l'on emprunte pour quitter s1 et quelque soit ce qui se passe après s1, on est assuré de revenir vers s1 en passant par par l'autre arête, puisque l'on est sur une chaîne. Ainsi, s1 est le dernier sommet de la chaîne puisqu'une fois revenu il n'y a plus d'issue.
Ce raisonnement s'applique aussi lorsque l'ordre du sommet s1 est 5, ce qui induit juste un aller retour de plus.""")

st.write("""Si l'on quitte s1 pour s2, alors on retrouve dans la même situation puisque s2 est aussi d'ordre impair et le même raisonnement implique que s2 lui aussi doit être le dernier sommet de la chaîne, ce qui est absurde. Il n'existe donc pas de chaîne eulerienne dans ce graphe.""")

st.write("""En particulier, il n'existe pas de cycle eulérien, une chaîne qui reviendrait à son point de départ, non plus.""")


# edges = ""
# edges = st.text_input('Add edges ("u_0,v_0 u_1, v_1 ...")')


# if edges:
#     for edge in edges.split():
#         u, v = [int(i) for i in edge.split(",")]
#         G.add_edge(u, v)

# G.draw(ax)
# st.pyplot(fig)
