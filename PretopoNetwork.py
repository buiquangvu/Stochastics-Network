'''
Created on Jun 23, 2015

@author: QUANGVU
'''
import networkx as nx
from networkx.classes.function import number_of_nodes, number_of_edges
# import matplotlib.pyplot as plt
# from networkx.classes.function import number_of_nodes, number_of_edges
#import gexf
#from networkx.readwrite.gexf import read_gexf
#import numpy as np

# construct family of neighborhood from set of Edges and set of relation
# relation = [relation1,relation2,...,relationp] for Graph
def NeighborhoodfromEdge(rel,G):
# construct family of neighborhood from set of Edges and set of relations for Graph (Undirected Graph)
    relation=rel
    Nodes=G.node.keys()
    B=[]

    for j in range(len(relation)):
        B.append({})
    for k in range(len(relation)):
        Edge_rel=[ (u,v,edata[relation[k]]) for u,v,edata in G.edges(data=True) if relation[k]in edata ]
        for node in Nodes:
            setofneighborhood=[]
            for i in range(len(Edge_rel)):
                if Edge_rel[i][0]==node:
                    setofneighborhood.append(Edge_rel[i][1])
                if Edge_rel[i][1]==node:
                    setofneighborhood.append(Edge_rel[i][0])
            B[k][node]=setofneighborhood
    return B  

# construct family of neighborhood from set of Edges and set of relation
# relation = [relation1,relation2,...,relationp] for Directed Graph 

def DiNeighborhoodfromEdge(rel,G):
# construct family of neighborhood from set of Edges and set of relations for Directed Graph 
    relation=rel
    Nodes=G.node.keys()
    B=[]
    for j in range(len(relation)):
        B.append({})
    for k in range(len(relation)):
        Edge_rel=[ (u,v,edata[relation[k]]) for u,v,edata in G.edges(data=True) if relation[k]in edata ]
        for node in Nodes:
            setofneighborhood=[]
            for i in range(len(Edge_rel)):
                if Edge_rel[i][1]==node:
                    setofneighborhood.append(Edge_rel[i][0])
            B[k][node]=setofneighborhood
    return B             

# construct family of neighborhood from set of Edges and set of relation
# relation = [relation1,relation2,...,relationp] for Directed Graph 
def DiNeighborhoodfromTwoGraph(G1,G2):
    relation=["relation1","relation2"]
    G=nx.MultiDiGraph()
    G.add_nodes_from(G1)
    G.add_edges_from(G1.edges(),relation1=1)
    G.add_edges_from(G2.edges(),relation2=2)
    Nodes=G.node.keys()
    B=[]
    for j in range(len(relation)):
        B.append({})
    for k in range(len(relation)):
        Edge_rel=[ (u,v,edata[relation[k]]) for u,v,edata in G.edges(data=True) if relation[k]in edata ]
        for node in Nodes:
            setofneighborhood=[]
            for i in range(len(Edge_rel)):
                if Edge_rel[i][1]==node:
                    setofneighborhood.append(Edge_rel[i][0])
            B[k][node]=setofneighborhood
    return B     


# Function to add element itself in Family of Neighborhood 
def Add_itself(E,B):
    for k in range(len(B)):
        for x in E:
            if x not in set(B[k][x]):
                B[k][x].append(x)

# Build general pseudo closure function
def pseudoclosure_general(E,B,A,pseudo_type=0,indexsetofrelation=0):
    # pseudo_type =0 for strong pseudo closure and pseudo_type = 1 for weak pseudo closure
    # indexsetofrelation : set of index of relations
    # indexsetofrelation = 0 if we use all relations; 
    Add_itself(E,B)
    aA=[]
    if indexsetofrelation ==0:
        indexsetofrelation=range(len(B))
    if pseudo_type==0:   
        for x in E :
            choose=True
            for k in indexsetofrelation:
                N=B[k][x]
                if len(set(N).intersection(set(A)))==0:
                    choose=False
                    break
            if choose:
                aA.append(x)           
    else:
        for x in E :
            choose=False
            for k in indexsetofrelation:
                N=B[k][x]
                if len(set(N).intersection(set(A)))!=0:
                    choose=True
                    break
            if choose:
                aA.append(x)
    return aA


# Build general pseudo closure function
def pseudoclosure_graph(E,B,A,pseudo_type=0,indexsetofrelation=0):
    # pseudo_type =0 for strong pseudo closure and pseudo_type = 1 for weak pseudo closure
    # indexsetofrelation : set of index of relations
    # indexsetofrelation = 0 if we use all relations; 
    Add_itself(E,B)
    aA=[]
    if indexsetofrelation ==0:
        indexsetofrelation=range(len(B))
    if pseudo_type==0:   
        for x in E :
            choose=True
            for k in indexsetofrelation:
                N=B[k][x]
                if len(set(N).intersection(set(A)))==0:
                    choose=False
                    break
            if choose:
                aA.append(x)           
    else:
        for x in E :
            choose=False
            for k in indexsetofrelation:
                N=B[k][x]
                if len(set(N).intersection(set(A)))!=0:
                    choose=True
                    break
            if choose:
                aA.append(x)
    return aA

# Function to compute family of neighborhood after  using pseudo closure
def neighborhood_family_pseudo_general(E,B,pseudo_type=0,indexsetofrelation=0 ):
    # pseudo_type =0 (default value) for strong pseudo closure
    # pseudo_type =! 0 for weak pseudo closure
    # indexsetofrelation : set of index of relations
    # indexsetofrelation = 0 (default value) if we use all relations; 
    B_new={}
    pseudo_type= pseudo_type
    indexsetofrelation=indexsetofrelation 
    for y in E:
        aAx=[]
        x=[]
        x.append(y)
        aAx=pseudoclosure_general(E,B,x,pseudo_type,indexsetofrelation)     
        B_new[y]=aAx
    return B_new

# Function to construct edge_list from family of neighborhood for undirected graph
def Graph_from_neighborhood(neighborhood_family):
# Function to construct edge_list from family of neighborhood for undirected graph
    G=nx.Graph()
    edge_list=[]
    for node_source in neighborhood_family:
        for node_target in range(len(neighborhood_family[node_source])):
            if str(neighborhood_family[node_source][node_target]) != str(node_source):
                edge=(node_source,neighborhood_family[node_source][node_target])
                edge_list.append(edge)
    G.add_edges_from(edge_list)
    return G

# Function to construct edge_list from family of neighborhood for directed graph
def diGraph_from_neighborhood(neighborhood_family):
# Function to construct edge_list from family of neighborhood for directed graph
    G=nx.DiGraph()
    edge_list=[]
    for node_source in neighborhood_family:
        G.add_node(node_source)
        for index_node_target in range(len(neighborhood_family[node_source])):
            if str(neighborhood_family[node_source][index_node_target]) != str(node_source):
                edge=(node_source,neighborhood_family[node_source][index_node_target])
                edge_list.append(edge)
    G.add_edges_from(edge_list)
    return G


G92=nx.read_adjlist("id-2000.txt")
print "2000"
print number_of_nodes(G92)
print number_of_edges(G92)
G93=nx.read_adjlist("id-2001.txt")
print "2001"
print number_of_nodes(G93)
print number_of_edges(G93)

G9293=nx.MultiGraph()
G9293.add_nodes_from(G92)
G9293.add_nodes_from(G93)
G9293.add_edges_from(G92.edges(),rel1=1)
G9293.add_edges_from(G93.edges(),rel2=2)
print "2000 and 2001"
print number_of_nodes(G9293)
print number_of_edges(G9293)
relation=["rel1","rel2"]
B9293=NeighborhoodfromEdge(relation,G9293)
print B9293
B9293_new=neighborhood_family_pseudo_general(G9293.node.keys(), B9293,1,0)
G9293_new=Graph_from_neighborhood(B9293_new)
   
print "2000 or 2001"
print number_of_nodes(G9293_new)
print number_of_edges(G9293_new)

nx.write_edgelist(G92, "2000-edgelist.txt")
nx.write_edgelist(G93, "2001-edgelist.txt")
# nx.write_edgelist(G9293_new, "2000or01-edgelist")
nx.write_edgelist(G9293_new, "2000or01-edgelist.txt")
# pos=nx.spring_layout(G93,iterations=100)
# nx.draw(G93,pos,node_size=500,with_labels=True)            
# plt.savefig("pretoponetwork.png") # save as png
#   
# plt.show()


# pos=nx.spring_layout(G9293_new,iterations=100)
# nx.draw(G9293_new,pos,node_size=500,with_labels=True)            
# plt.savefig("pretoponetwork.png") # save as png
#    
# plt.show()
 
# 
#  
# G94=nx.read_adjlist("id-article-2002.txt")
#  
# G929394=nx.MultiGraph()
# G929394.add_nodes_from(G92)
# G929394.add_nodes_from(G93)
# G929394.add_nodes_from(G94)
# G929394.add_edges_from(G92.edges(),rel1=1)
# G929394.add_edges_from(G93.edges(),rel2=2)
# G929394.add_edges_from(G94.edges(),rel2=3)
# relation=["rel1","rel2","rel3"]
# B929394=NeighborhoodfromEdge(relation,G929394)
# B929394_new=neighborhood_family_pseudo_general(G929394.node.keys(), B929394,1,0)
# G929394_new=Graph_from_neighborhood(B929394_new)
# print "2002"
# print number_of_nodes(G94)
# print number_of_edges(G94)
# print "================="
# print number_of_nodes(G929394_new)
# print number_of_edges(G929394_new)
 


# Create multi -relation network from many Graphs
#===============================================================================

# G1 = nx.Graph()
# G1.add_nodes_from([1,2,3,4])
# G1.add_edges_from([(1,2),(1,3),(2,4),(3,4)])
# 
# G2 = nx.Graph()
# G2.add_nodes_from([1,2,3,4])
# G2.add_edges_from([(1,2),(1,3),(2,3),(3,4)])
#    
# G3 = nx.Graph()
# G3.add_nodes_from([1,2,3,4,5])
# G3.add_edges_from([(1,2),(1,4),(2,3),(4,3),(1,5)])
#   
# G=nx.MultiGraph()
# G.add_nodes_from(G1)
# G.add_edges_from(G1.edges(),rel1=1)
# G.add_edges_from(G2.edges(),rel2=2)
# G.add_edges_from(G3.edges(),rel3=3)
#     
# relation=["rel1","rel2","rel3"] 
# relation1=["rel1","rel2"]
# B=NeighborhoodfromEdge(relation,G)
# indexofrelation=[0,1,2]
# print B
#  
# B_new_general=neighborhood_family_pseudo_general(G.node.keys(), B,0,indexofrelation)
# print "family of neighborhood after 01 step using pseudo closure: ", B_new_general
# 
# G_general=Graph_from_neighborhood(B_new_general)
#     
#     
# # Graph Layout with multi graph in layout
#     
# pos=nx.spring_layout(G,iterations=100)
# plt.clf()
# plt.subplot(221)
# plt.title('Relation 1')
# nx.draw(G1,pos,node_size=500,with_labels=True)  
# plt.subplot(222)
# plt.title('Relation 2')
# nx.draw(G2,pos,node_size=500,with_labels=True)
#     
# plt.subplot(223)
# plt.title('Relation 3')
# nx.draw(G3,pos,node_size=500,with_labels=True)
#            
#           
# plt.subplot(224)
# plt.title('general relation')
# nx.draw(G_general,pos,node_size=500,with_labels=True)
#      
# nx.draw(G_general,pos,node_size=500,with_labels=True)            
# plt.savefig("pretoponetwork.png") # save as png
#   
# plt.show()




# try with Directed Graph
# G1 = nx.DiGraph()
# G1.add_nodes_from([1,2,3,4])
# G1.add_edges_from([(1,2),(1,3),(2,4),(3,4)])
# 
# G2 = nx.DiGraph()
# G2.add_nodes_from([1,2,3,4])
# G2.add_edges_from([(1,2),(1,3),(2,3),(3,4)])
#    
# G3 = nx.DiGraph()
# G3.add_nodes_from([1,2,3,4,5])
# G3.add_edges_from([(1,2),(1,4),(2,3),(4,3),(1,5)])
#   
# G=nx.MultiDiGraph()
# G.add_nodes_from(G1)
# G.add_edges_from(G1.edges(),rel1=1)
# G.add_edges_from(G2.edges(),rel2=2)
# G.add_edges_from(G3.edges(),rel3=3)
#     
# relation=["rel1","rel2","rel3"] 
# relation1=["rel1","rel2"]
# B=DiNeighborhoodfromEdge(relation,G)
# indexofrelation=[0,1,2]
# print B
#  
# B_new_general=neighborhood_family_pseudo_general(G.node.keys(), B,0,indexofrelation)
# print "family of neighborhood after 01 step using pseudo closure: ", B_new_general
# 
# G_general=diGraph_from_neighborhood(B_new_general)
#     
#     
# # Graph Layout with multi graph in layout
#     
# pos=nx.spring_layout(G,iterations=100)
# plt.clf()
# plt.subplot(221)
# plt.title('Relation 1')
# nx.draw(G1,pos,node_size=500,with_labels=True)  
# plt.subplot(222)
# plt.title('Relation 2')
# nx.draw(G2,pos,node_size=500,with_labels=True)
#     
# plt.subplot(223)
# plt.title('Relation 3')
# nx.draw(G3,pos,node_size=500,with_labels=True)
#            
#           
# plt.subplot(224)
# plt.title('general relation')
# nx.draw(G_general,pos,node_size=500,with_labels=True)
#      
# nx.draw(G_general,pos,node_size=500,with_labels=True)            
# plt.savefig("pretoponetwork.png") # save as png
#   
# plt.show()





# Create multi -relation network directly
# G=nx.MultiGraph()
# #G.add_nodes_from(["a","b","c","d"])
# edge_list=[("a","b",{"rel1":1}),("a","b",{"rel2":2}),("b","c",{"rel1":1}),("a","c",{"rel2":2}),("c","d",{"rel1":1}),("c","d",{"rel2":2}),("d","a",{"rel1":1}),("b","d",{"rel2":2})]
# edge_list2=[("a","b",{"rel1":1}),("a","b",{"rel2":2}),("b","c",{"rel1":1}),("b","c",{"rel2":2}),("a","c",{"rel2":2}),("c","d",{"rel1":1}),("c","d",{"rel2":2}),("d","a",{"rel1":1}),("d","a",{"rel2":2}),("b","d",{"rel2":2})] 
# G.add_edges_from(edge_list2)



# H1 = nx.DiGraph()
# H1.add_nodes_from([1,2,3,4])
# H1.add_edges_from([(1,2),(1,3),(2,4),(3,4)])
# nx.write_edgelist(H1, "test.edgelist")
# 
# G1=nx.read_edgelist("test.edgelist",nodetype=int,create_using=nx.DiGraph())
# print G1.edge