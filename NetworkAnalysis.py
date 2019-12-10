import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams, matplotlib
import seaborn as sb
import networkx as nx

#%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

G = nx.Graph()
G.add_node(1)
nx.draw(G)
G.add_nodes_from([2,3,4,5,6,8,9,12,15,16])
nx.draw(G)

G.add_edges_from([(2,4),(2,6),(2,8),(2,12),(2,16),(3,6),(3,9), (3,12),(3,15),(4,8),(4,12),(4,16),(6,12),(8,16)])
nx.draw(G)

nx.draw_circular(G)

nx.draw_spring(G)

nx.draw_circular(G, node_color='bisque', with_labels=True)

G.remove_node(1)
nx.draw_circular(G, node_color='bisque', with_labels=True)
sum_stats = nx.info(G)
print(sum_stats)

print(nx.degree(G))

G = nx.complete_graph(25)
nx.draw(G, node_color='bisque', with_labels=True)

G = nx.gnc_graph(7, seed=25)
nx.draw(G, node_color='bisque', with_labels=True)

ego_G = nx.ego_graph(G, 3, radius=5)
nx.draw(G, node_color='bisque', with_labels=True)

# SIMULATING SOCIAL NETWORK
DG = nx.gn_graph(7, seed=25)
for line in nx.generate_edgelist(DG, data=False): print(line)
print(DG.node[0])

DG.node[0]['name'] = 'Alice'
print(DG.node[0])

DG.node[1]['name'] = 'Bob'
DG.node[2]['name'] = 'Claire'
DG.node[3]['name'] = 'Dennis'
DG.node[4]['name'] = 'Esther'
DG.node[5]['name'] = 'Frank'
DG.node[6]['name'] = 'George'

DG.add_nodes_from([(0,{'age':25}),(1,{'age':31}),(2,{'age':18}),(3,{'age':47}),(4,{'age':22}),
                   (5,{'age':23}),(6,{'age':50})])
print DG.node[0]

DG.node[0]['gender'] = 'f'
DG.node[1]['gender'] = 'm'
DG.node[2]['gender'] = 'f'
DG.node[3]['gender'] = 'm'
DG.node[4]['gender'] = 'f'
DG.node[5]['gender'] = 'm'
DG.node[6]['gender'] = 'm'

nx.draw_circular(DG, node_color='bisque', with_labels=True)

labeldict = {0: 'Alice',1:'Bob',2:'Claire',3:'Dennis',4:'Esther',5:'Frank',6:'George'}

nx.draw_circular(DG, labels=labeldict, node_color='bisque', with_labels=True)

G = DG.to_undirected()
nx.draw_spectral(G, labels=labeldict, node_color='bisque', with_labels=True)

print nx.info(DG)

DG.degree()

nx.draw_circular(DG, node_color='bisque', with_labels=True)
DG.successors(3)
DG.neighbors(4)
G.neighbors(4)