'''
Created on Jun 23, 2015

@author: QUANGVU


'''
import networkx as nx
# import matplotlib.pyplot as plt
from networkx.classes.function import number_of_nodes, number_of_edges

def constructGraph_Year(setofGraph):
    G = nx.Graph()
    for H in setofGraph:
        G.add_nodes_from(H)
    SetofNode=G.node.keys()
    print "len set of Node", len(SetofNode)
    for i in range(len(SetofNode)):
        print "loop", i
        for j in range(i+1,len(SetofNode)):
            count=0
            for H in setofGraph:
                if (SetofNode[i],SetofNode[j]) in nx.edges(H,SetofNode[i]):
                    count=count+1
            if count > 0:
                G.add_edge(SetofNode[i],SetofNode[j], numofyear = count)
    return G

def StrongGraph(setofGraph,k):
    G=constructGraph_Year(setofGraph)
    SetofNode=G.node.keys()
    edge_list=[]
    G_strong=nx.Graph()
    for i in range(len(SetofNode)):
        for j in range(i+1,len(SetofNode)):
            if ((SetofNode[i],SetofNode[j]) in nx.edges(G,SetofNode[i])):
                if (G[SetofNode[i]][SetofNode[j]]["numofyear"] >= k):
                    edge_list.append((SetofNode[i],SetofNode[j]))               
    G_strong.add_edges_from(edge_list)
    return G_strong          

def WeakGraph(setofGraph,k):
    G=constructGraph_Year(setofGraph)
    SetofNode=G.node.keys() 
    edge_list=[]
    G_weak=nx.Graph()
    for i in range(len(SetofNode)):
        for j in range(i+1,len(SetofNode)):
            if ((SetofNode[i],SetofNode[j]) in nx.edges(G,SetofNode[i])):
                if (G[SetofNode[i]][SetofNode[j]]["numofyear"] <= k):
                    edge_list.append((SetofNode[i],SetofNode[j]))              
    G_weak.add_edges_from(edge_list)
    return G_weak  


def SemiStrongGraph(setofGraph,k1,k2):
    G=constructGraph_Year(setofGraph)
    SetofNode=G.node.keys() 
    edge_list=[]
    G_weak=nx.Graph()
    for i in range(len(SetofNode)):
        for j in range(i+1,len(SetofNode)):
            if ((SetofNode[i],SetofNode[j]) in nx.edges(G,SetofNode[i])):
                if (k1 <= G[SetofNode[i]][SetofNode[j]]["numofyear"] <= k2):
                    edge_list.append((SetofNode[i],SetofNode[j]))              
    G_weak.add_edges_from(edge_list)
    return G_weak  


# G00=nx.read_adjlist("id-article-2000.txt")
# G01=nx.read_adjlist("id-article-2001.txt")
# G02=nx.read_adjlist("id-article-2002.txt")
# G03=nx.read_adjlist("id-article-2003.txt")
# G04=nx.read_adjlist("id-article-2004.txt")
# G05=nx.read_adjlist("id-article-2005.txt")


# G89before=nx.read_adjlist("id-1989before.txt")
# G9094=nx.read_adjlist("id-1990-1994.txt")
# G9599=nx.read_adjlist("id-1995-1999.txt")
# G00=nx.read_adjlist("id-2000.txt")
# G01=nx.read_adjlist("id-2001.txt")
# G02=nx.read_adjlist("id-2002.txt")
# G03=nx.read_adjlist("id-2003.txt")
# G04=nx.read_adjlist("id-2004.txt")
# G05=nx.read_adjlist("id-2005.txt")
# G06=nx.read_adjlist("id-2006.txt")
# G07=nx.read_adjlist("id-2007.txt")
# G08=nx.read_adjlist("id-2008.txt")
# G09=nx.read_adjlist("id-2009.txt")
# G10=nx.read_adjlist("id-2010.txt")
# G11=nx.read_adjlist("id-2011.txt")
# G12=nx.read_adjlist("id-2012.txt")
# G13=nx.read_adjlist("id-2013.txt")
# G14=nx.read_adjlist("id-2014.txt")
# G15=nx.read_adjlist("id-2015.txt")
# setofGraph=[G00,G01,G02,G03,G04,G05,G06,G07,G08,G09,G10,G11,G12]

# setofGraph=[G11,G12,G13,G14,G15]
# G_str3=StrongGraph(setofGraph,3)
# nx.write_edgelist(G_str3, "G_str3-11-15.txt")
# 
# G=constructGraph_Year(setofGraph)
# nx.write_edgelist(G, "G11-15.txt")

# G=nx.read_edgelist("G00-12-edgelist.txt")
# G_str=nx.read_edgelist("G_str5-edgelist.txt")
# G_weak=nx.read_edgelist("G_w1-edgelist.txt")
# G_semistr=nx.read_edgelist("G_semistr24-edgelist.txt")
# authorid="2795"


G1=nx.read_edgelist("G10-14.txt")
G2=nx.read_edgelist("G11-15.txt")
G_str1=nx.read_edgelist("G_str3-10-14.txt")
G_str2=nx.read_edgelist("G_str3-11-15.txt")
# 
# 
E1=G_str1.edge
print E1
print len(E1)
print len(G_str1.node)
count1=0
lenedge=0
for i in G_str1.node:
#     print G_str1.edges(i)
    lenedge+=len(G_str1.edges(i))
    for j in G_str1.edges(i):
        if j in G_str2.edges(i):
            count1+=1
print "number of edges in intersection:",count1
print "number of edges in G00-04:",lenedge
  
  
count2=0
for i in G_str1.node:
    for j in G_str1.edges(i):
        if j not in G_str2.edges(i):
            count2+=1
print "number of edges not remain strong ties:",count2
  
count3=0
lenedge2=0
for i in G_str2.node:
    lenedge2+=len(G_str2.edges(i))
    for j in G_str2.edges(i):
        if j not in G_str1.edges(i):
            count3+=1
print "number of new strong edges:",count3
print "number of edges in G01-05:", lenedge2




# print number_of_nodes(G),number_of_edges(G)
# print number_of_nodes(G_str),number_of_edges(G_str)
# print number_of_nodes(G_semistr),number_of_edges(G_semistr)
# print number_of_nodes(G_weak),number_of_edges(G_weak)

# N_G_10=G.neighbors("10")

# N_G_10=G.neighbors("10")
# N_G_str_10=G_str.neighbors("10")
# N_G_weak_10=G_weak.neighbors("10")
# N_G_semistr_10=G_semistr.neighbors("10")
# print "number of co-author of 10 (Marc)", len(N_G_10)
# print "number of strong conected co-author of 10 (Marc)", len(N_G_str_10)
# print "number of semi strong conected co-author of 10 (Marc)", len(N_G_semistr_10)
# print "number of weak conected co-author of 10 (Marc)", len(N_G_weak_10)


#===============================================================================
# compute the proportion of number of triadic is triadic closure  p = m/n for the strong connected 
# check triadic closure theorem: B,C is strong tie of A, It exists a tie (strong or weak) between B,C
#===============================================================================
# N_G_10=G.neighbors(authorid)
# N_G_str_10=G_str.neighbors(authorid)
# print "number of co-author of 10 (Marc)", len(N_G_10)
# print "number of strong conected co-author of 10 (Marc)", len(N_G_str_10)
# number_of_strongties=len(N_G_str_10)
# triadic_closure=0
# for i in range(len(N_G_str_10)):
#     for j in range(i+1,len(N_G_str_10)):
#         if (N_G_str_10[i],N_G_str_10[j]) in nx.edges(G,N_G_str_10[i]):
#             triadic_closure+=1
# p=200*triadic_closure/(number_of_strongties*(number_of_strongties-1))
# print triadic_closure
# print (number_of_strongties*(number_of_strongties-1))/2
# print p



#===============================================================================
# compute the proportion of number of triadic is triadic closure  p = m/n for the semi-strong connected 
# check triadic closure theorem: B,C is strong tie of A, It exists a tie (strong or weak) between B,C
#===============================================================================
# N_G_10=G.neighbors(authorid)
# N_G_semistr_10=G_semistr.neighbors(authorid)
# print "number of co-author of 10 (Marc)", len(N_G_10)
# print "number of semi -  strong conected co-author of 10 (Marc)", len(N_G_semistr_10)
# number_of_semistrongties=len(N_G_semistr_10)
# triadic_closure=0
# for i in range(len(N_G_semistr_10)):
#     for j in range(i+1,len(N_G_semistr_10)):
#         if (N_G_semistr_10[i],N_G_semistr_10[j]) in nx.edges(G,N_G_semistr_10[i]):
#             triadic_closure+=1
# p=200*triadic_closure/(number_of_semistrongties*(number_of_semistrongties-1))
# print triadic_closure
# print (number_of_semistrongties*(number_of_semistrongties-1))/2
# print p


#===============================================================================
# compute the proportion of number of triadic is triadic closure  p = m/n for the weak connected 
# check triadic closure theorem: B,C is strong tie of A, It exists a tie (strong or weak) between B,C
#===============================================================================
# N_G_10=G.neighbors(authorid)
# N_G_weak_10=G_weak.neighbors(authorid)
# print "number of co-author of 10 (Marc)", len(N_G_10)
# print "number of weak conected co-author of 10 (Marc)", len(N_G_weak_10)
# number_of_weakties=len(N_G_weak_10)
# triadic_closure=0
# for i in range(len(N_G_weak_10)):
#     for j in range(i+1,len(N_G_weak_10)):
#         if (N_G_weak_10[i],N_G_weak_10[j]) in nx.edges(G,N_G_weak_10[i]):
#             triadic_closure+=1
# p=200*triadic_closure/(number_of_weakties*(number_of_weakties-1))
# print triadic_closure
# print (number_of_weakties*(number_of_weakties-1))/2
# print p
# 
# print "-------------------------------------"
#===============================================================================
# compute the average of number of neighborhood of neighborhood of x is also neighborhood of x
# for the strong and weak connected 
# in the same network
#===============================================================================
# N_G_str_10=G_str.neighbors(authorid)
# N_G_semistr_10=G_semistr.neighbors(authorid)
# N_G_weak_10=G_weak.neighbors(authorid)
# N_G_10=G.neighbors(authorid)
# print "number of co-author of 10 (Marc)", len(N_G_10)
# print "number of strong conected co-author of 10 (Marc)", len(N_G_str_10)
# print "number of semi strong conected co-author of 10 (Marc)", len(N_G_semistr_10)
# print "number of weak conected co-author of 10 (Marc)", len(N_G_weak_10)
#  
# # for strong connected
# sum_str=0
# for x in N_G_str_10:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G_10))
#     sum_str+=len(trideo)
# aver_str=sum_str/len(N_G_str_10)
# print sum_str
# print len(N_G_str_10)
# print aver_str
#   
#   
# # for semi strong connected
# sum_semistr=0
# for x in N_G_semistr_10:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G_10))
#     sum_semistr+=len(trideo)
# aver_semistr=sum_semistr/(len(N_G_semistr_10))
# print sum_semistr
# print len(N_G_semistr_10)
# print aver_semistr
#   
#   
# # # for weak connected
# sum_w=0
# for x in N_G_weak_10:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G_10))
#     sum_w+=len(trideo)
# aver_w=sum_w/(len(N_G_weak_10))
# print sum_w
# print len(N_G_weak_10)
# print aver_w


# #Year 2013
# #===============================================================================
# # compute the average of number of neighborhood of neighborhood of x is also neighborhood of x
# # for the strong and weak connected 
# # in the future network
# #===============================================================================
# print "-----------------2013--------------------"
# 
# G13=nx.read_adjlist("id-2013.txt")
# N_G_10=G.neighbors(authorid)
# N_G13_10=G13.neighbors(authorid)
# N_G_str_10=G_str.neighbors(authorid)
# N_G_str_10_intersection=set(N_G_str_10).intersection(G13.nodes())
# N_G_semistr_10=G_semistr.neighbors(authorid)
# N_G_semistr_10_intersection=set(N_G_semistr_10).intersection(G13.nodes())
# N_G_weak_10=G_weak.neighbors(authorid)
# N_G_weak_10_intersection=set(N_G_weak_10).intersection(G13.nodes())
#   
# print "number of co-author of 10 (Marc)", len(N_G_10)
# print "number of co-author of 10 (Marc) in year 2013:", len(N_G13_10)
# print "number of strong conected co-author of 10 (Marc):", len(N_G_str_10)
# print "number of semi strong conected co-author of 10 (Marc):", len(N_G_semistr_10)
# print "number of weak conected co-author of 10 (Marc):", len(N_G_weak_10)
# print "number of strong conected co-author of 10 (Marc) intersection 2000-2012 and 2013:", len(N_G_str_10_intersection)
# print "number of semi strong conected co-author of 10 (Marc) intersection 2000-2012 and 2013:", len(N_G_semistr_10_intersection)
# print "number of weak conected co-author of 10 (Marc) intersection 2000-2012 and 2013:", len(N_G_weak_10_intersection)
# #  
# # for strong connected
# sum_str_2013=0
# for x in N_G_str_10_intersection:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G13_10))
#     sum_str_2013+=len(trideo)
# aver_str_2013=sum_str_2013/len(N_G_str_10_intersection)
# print sum_str_2013
# print len(N_G_str_10_intersection)
# print aver_str_2013
#  
 
 
# for semi strong connected
# sum_semistr_2013=0
# for x in N_G_semistr_10_intersection:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G13_10))
#     sum_semistr_2013+=len(trideo)
# aver_semistr_2013=sum_semistr_2013/len(N_G_semistr_10_intersection)
# print sum_semistr_2013
# print len(N_G_semistr_10_intersection)
# print aver_semistr_2013
#  
# # for weak connected
#  
# sum_w_2013=0
# for x in N_G_weak_10_intersection:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G13_10))
#     sum_w_2013+=len(trideo)
# aver_w_2013=sum_w_2013/len(N_G_weak_10_intersection)
# print sum_w_2013
# print len(N_G_weak_10_intersection)
# print aver_w_2013
 

# #Year 2014
# #===============================================================================
# # compute the average of number of neighborhood of neighborhood of x is also neighborhood of x
# # for the strong and weak connected 
# # in the future network
# #===============================================================================
# print "-----------------2014--------------------"
# G14=nx.read_adjlist("id-2014.txt")
# N_G_10=G.neighbors(authorid)
# N_G14_10=G14.neighbors(authorid)
# N_G_str_10=G_str.neighbors(authorid)
# N_G_str_10_intersection=set(N_G_str_10).intersection(G14.nodes())
# N_G_semistr_10=G_semistr.neighbors(authorid)
# N_G_semistr_10_intersection=set(N_G_semistr_10).intersection(G14.nodes())
# N_G_weak_10=G_weak.neighbors(authorid)
# N_G_weak_10_intersection=set(N_G_weak_10).intersection(G14.nodes())
#   
# print "number of co-author of 10 (Marc)", len(N_G_10)
# print "number of co-author of 10 (Marc) in year 2014:", len(N_G14_10)
# print "number of strong conected co-author of 10 (Marc):", len(N_G_str_10)
# print "number of semi strong conected co-author of 10 (Marc):", len(N_G_semistr_10)
# print "number of weak conected co-author of 10 (Marc):", len(N_G_weak_10)
# print "number of strong conected co-author of 10 (Marc) intersection 2000-2012 and 2014:", len(N_G_str_10_intersection)
# print "number of semi strong conected co-author of 10 (Marc) intersection 2000-2012 and 2014:", len(N_G_semistr_10_intersection)
# print "number of weak conected co-author of 10 (Marc) intersection 2000-2012 and 2014:", len(N_G_weak_10_intersection)
#   
# # for strong connected
# sum_str_2014=0
# for x in N_G_str_10_intersection:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G14_10))
#     sum_str_2014+=len(trideo)
# aver_str_2014=sum_str_2014/len(N_G_str_10_intersection)
# print sum_str_2014
# print len(N_G_str_10_intersection)
# print aver_str_2014
#  
#  
#  
# # for semi strong connected
# sum_semistr_2014=0
# for x in N_G_semistr_10_intersection:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G14_10))
#     sum_semistr_2014+=len(trideo)
# aver_semistr_2014=sum_semistr_2014/len(N_G_semistr_10_intersection)
# print sum_semistr_2014
# print len(N_G_semistr_10_intersection)
# print aver_semistr_2014
#  
# # for weak connected
#  
# sum_w_2014=0
# for x in N_G_weak_10_intersection:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G14_10))
#     sum_w_2014+=len(trideo)
# aver_w_2014=sum_w_2014/len(N_G_weak_10_intersection)
# print sum_w_2014
# print len(N_G_weak_10_intersection)
# print aver_w_2014



# #Year 2013
# #===============================================================================
# # compute the propotion of neighborhood of neighborhood of x that is not neighbor of x in G0012 
# is also neighborhood of x in 2013 
# # for the strong and weak connected 
# # in the future network
# #===============================================================================
# print "-----------------proportion 2013--------------------"
# 
# G13=nx.read_adjlist("id-2013.txt")
# N_G_10=G.neighbors(authorid)
# N_G13_10=G13.neighbors(authorid)
# N_G_str_10=G_str.neighbors(authorid)
# # N_G_str_10_intersection=set(N_G_str_10).intersection(G13.nodes())
# # N_G_semistr_10=G_semistr.neighbors(authorid)
# # N_G_semistr_10_intersection=set(N_G_semistr_10).intersection(G13.nodes())
# # N_G_weak_10=G_weak.neighbors(authorid)
# # N_G_weak_10_intersection=set(N_G_weak_10).intersection(G13.nodes())
#  
# 
# # for strong connected
# 
# beneigh=[]
# for x in N_G_10:
#     Neigh=G.neighbors(x)
#     for y in Neigh:
#         if authorid in G.neighbors(y):
#             beneigh.append(y)
# set_beneigh = set(beneigh)        
# print set_beneigh  
# print len(set_beneigh)  
# print len(beneigh)    
# 
# notneigh=[]
# for x in N_G_10:
#     Neigh=G.neighbors(x)
#     for y in Neigh:
#         if authorid not in G.neighbors(y):
#             notneigh.append(y)
# set_notneigh = set(notneigh)        
# print  set_notneigh  
# print len(set_notneigh)  
# print len(notneigh) 
# print len(G.node)
# print len(N_G_10)
# 
# print len(G13.node)
# print G13.neighbors(authorid)
# print len(G13.neighbors(authorid))
# print "----new----"
# beneigh13=[]
# for x in beneigh:
#     if x in G13.node: 
#         if authorid in G13.neighbors(x):
#             beneigh13.append(x)
# set_beneigh13 = set(beneigh13)        
# print set_beneigh13  
# print len(set_beneigh13)  
# print len(beneigh13)    

# sum_str_2013=0
# for x in N_G_str_10_intersection:
#     Neigh=G.neighbors(x)
# # neighberhood of x also neighborhood of 10 
#     trideo=set(Neigh).intersection(set(N_G13_10))
#     sum_str_2013+=len(trideo)
# aver_str_2013=sum_str_2013/len(N_G_str_10_intersection)
# print sum_str_2013
# print len(N_G_str_10_intersection)
# print aver_str_2013



# Write file in edgeslist
# nx.write_edgelist(G89before, "1989-edgelist.txt")
# nx.write_edgelist(G9094, "90-94-edgelist.txt")
# nx.write_edgelist(G9599, "95-99-edgelist.txt")
# nx.write_edgelist(G00, "2000-edgelist.txt")
# nx.write_edgelist(G01, "2001-edgelist.txt")
# nx.write_edgelist(G02, "2002-edgelist.txt")
# nx.write_edgelist(G03, "2003-edgelist.txt")
# nx.write_edgelist(G04, "2004-edgelist.txt")
# nx.write_edgelist(G05, "2005-edgelist.txt")
# nx.write_edgelist(G06, "2006-edgelist.txt")
# nx.write_edgelist(G07, "2007-edgelist.txt")
# nx.write_edgelist(G08, "2008-edgelist.txt")
# nx.write_edgelist(G09, "2009-edgelist.txt")
# nx.write_edgelist(G10, "2010-edgelist.txt")
# nx.write_edgelist(G11, "2011-edgelist.txt")
# nx.write_edgelist(G12, "2012-edgelist.txt")
# nx.write_edgelist(G13, "2013-edgelist.txt")
# nx.write_edgelist(G14, "2014-edgelist.txt")
# nx.write_edgelist(G15, "2015-edgelist.txt")


# G_str1=StrongGraph(setofGraph,1)
# G_str2=StrongGraph(setofGraph,2)
# G_str3=StrongGraph(setofGraph,3)
# G_str4=StrongGraph(setofGraph,4)
# G_str5=StrongGraph(setofGraph,5)
# G_str6=StrongGraph(setofGraph,6)
# G_str7=StrongGraph(setofGraph,7)
# G_str8=StrongGraph(setofGraph,8)
# G_str9=StrongGraph(setofGraph,9)
# G_str10=StrongGraph(setofGraph,10)
# G_str11=StrongGraph(setofGraph,11)
# G_str12=StrongGraph(setofGraph,12)
# G_str13=StrongGraph(setofGraph,13)
# G_str14=StrongGraph(setofGraph,14)
# G_str15=StrongGraph(setofGraph,15)
# G_str16=StrongGraph(setofGraph,16)
# G_str17=StrongGraph(setofGraph,17)
# G_str18=StrongGraph(setofGraph,18)
# G_str19=StrongGraph(setofGraph,19)



# nx.write_edgelist(G_str3, "G_str3-02-06.txt")

# nx.write_edgelist(G_str1, "G_str1-edgelist.txt")
# nx.write_edgelist(G_str2, "G_str2-edgelist.txt")
# nx.write_edgelist(G_str3, "G_str3-edgelist.txt")
# nx.write_edgelist(G_str4, "G_str4-edgelist.txt")
# nx.write_edgelist(G_str5, "G_str5-edgelist.txt")
# nx.write_edgelist(G_str6, "G_str6-edgelist.txt")
# nx.write_edgelist(G_str7, "G_str7-edgelist.txt")
# nx.write_edgelist(G_str8, "G_str8-edgelist.txt")
# nx.write_edgelist(G_str9, "G_str9-edgelist.txt")
# nx.write_edgelist(G_str10, "G_str10-edgelist.txt")
# nx.write_edgelist(G_str11, "G_str11-edgelist.txt")
# nx.write_edgelist(G_str12, "G_str12-edgelist.txt")
# nx.write_edgelist(G_str13, "G_str13-edgelist.txt")
# nx.write_edgelist(G_str14, "G_str14-edgelist.txt")
# nx.write_edgelist(G_str15, "G_str15-edgelist.txt")
# nx.write_edgelist(G_str16, "G_str16-edgelist.txt")
# nx.write_edgelist(G_str17, "G_str17-edgelist.txt")
# nx.write_edgelist(G_str18, "G_str18-edgelist.txt")
# nx.write_edgelist(G_str19, "G_str19-edgelist.txt")

# G_w1=WeakGraph(setofGraph,1)
# G_w2=WeakGraph(setofGraph,2)
# G_w3=WeakGraph(setofGraph,3)
# G_w4=WeakGraph(setofGraph,4)
# G_w5=WeakGraph(setofGraph,5)
# G_w6=WeakGraph(setofGraph,6)
# G_w7=WeakGraph(setofGraph,7)
# G_w8=WeakGraph(setofGraph,8)
# G_w9=WeakGraph(setofGraph,9)
# G_w10=WeakGraph(setofGraph,10)
# G_w11=WeakGraph(setofGraph,11)

# nx.write_edgelist(G_w1, "G_w1-edgelist.txt")
# nx.write_edgelist(G_w2, "G_w2-edgelist.txt")
# nx.write_edgelist(G_w3, "G_w3-edgelist.txt")
# nx.write_edgelist(G_w4, "G_w4-edgelist.txt")
# nx.write_edgelist(G_w5, "G_w5-edgelist.txt")
# nx.write_edgelist(G_w6, "G_w6-edgelist.txt")
# nx.write_edgelist(G_w7, "G_w7-edgelist.txt")
# nx.write_edgelist(G_w8, "G_w8-edgelist.txt")
# nx.write_edgelist(G_w9, "G_w9-edgelist.txt")
# nx.write_edgelist(G_w10, "G_w10-edgelist.txt")
# nx.write_edgelist(G_w11, "G_w11-edgelist.txt")
# G_w12=WeakGraph(setofGraph,12)
# G_w13=WeakGraph(setofGraph,13)
# G_w14=WeakGraph(setofGraph,14)
# G_w15=WeakGraph(setofGraph,15)
# 
# nx.write_edgelist(G_w12, "G_w12-edgelist.txt")
# nx.write_edgelist(G_w13, "G_w13-edgelist.txt")
# nx.write_edgelist(G_w14, "G_w14-edgelist.txt")
# nx.write_edgelist(G_w15, "G_w15-edgelist.txt")



# G_semistr24=SemiStrongGraph(setofGraph,2,4)
# nx.write_edgelist(G_semistr24, "G_semistr24-edgelist.txt")
# G_semistr25=SemiStrongGraph(setofGraph,2,5)
# nx.write_edgelist(G_semistr25, "G_semistr25-edgelist.txt")
# print G_semistr24.Nodes()
# print len(G_semistr24.Nodes())

# pos=nx.spring_layout(G_str5,iterations=100)
# nx.draw(G_str5,pos,node_size=500,with_labels=True)            
# plt.show()






# G1 = nx.Graph()
# G1.add_nodes_from([1,2,3,4])
# G1.add_edges_from([(1,2),(1,3),(2,4),(3,4)])
# G2 = nx.Graph()
# G2.add_nodes_from([1,2,3,4])
# G2.add_edges_from([(1,2),(1,3),(2,3),(3,4)])
#     
# G3 = nx.Graph()
# G3.add_nodes_from([1,2,3,4,5])
# G3.add_edges_from([(1,2),(1,4),(2,3),(4,3),(1,5)])
# 
# setofGraph=[G1,G2,G3]
# G=constructGraph_Year(setofGraph)
# G_str=StrongGraph(setofGraph,2)
# print G_str.node.keys()
# print G_str.edge
# G_w=WeakGraph(setofGraph,2)
# print G_w.node.keys()
# print G_w.edge



