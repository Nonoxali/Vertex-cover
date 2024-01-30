def Mlist(M):
    gdict={}
    for i in range(M.shape[0]):
        gdict[i]=[]
        for j in range(M.shape[0]):
            if M[i][j]!=0:
                gdict[i].append(j)
    return gdict

def Transfo_Dict_To_Mat(dict):
    import numpy as np
    L=list(dict)
    o=len(L)
    M=np.zeros((o,o),dtype = int)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] in dict[L[j]]:
                M[i][j]=1
    return M

def deg(G,i):
        deg = 0
        for j in G[i]:
            deg += j
        return deg

def alldeg(G):
        tab = []
        for i in range (len(G)):
            tab.append(deg(G,i))
        return tab
import copy

def getE(self):
    u=[]
    for i in list(self.keys()):
        for j in self[i]:
            if (i,j) and (j,i) not in u:
                u.append((i,j))
    return u

#some graphs
graph = {'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['a', 'd'], 'd': ['b', 'c', 'e'], 'e': ['d', 'o'], 'o': ['e', 'coucou'], 'coucou': ['o']}

triang={"a":["b","c"],"b":["a","c"],"c":["b","a"]}

lobster={0: [1, 16], 1: [0, 2], 2: [1, 3], 3: [2, 4, 18], 4: [3, 5, 19], 5: [4, 6, 21], 6: [5, 7], 7: [6, 8, 23], 8: [7, 9, 25], 9: [8, 10], 10: [9, 11, 27], 11: [10, 12, 29], 12: [11, 13, 31], 13: [12, 14, 33], 14: [13, 15, 35], 15: [14], 16: [0, 17], 17: [16], 18: [3], 19: [4, 20], 20: [19], 21: [5, 22], 22: [21], 23: [7, 24], 24: [23], 25: [8, 26], 26: [25], 27: [10, 28], 28: [27], 29: [11, 30], 30: [29], 31: [12, 32], 32: [31], 33: [13, 34], 34: [33], 35: [14]}

box={1:[2,3,4],2:[1,3],3:[1,2,4],4:[1,3],}

crate={1:[2,3,5],2:[1,4,5],3:[1,4,5],4:[2,3,5],5:[1,2,3,4]}

triangdev = np.array([[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]])

Etoile = np.array([[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]])

Etoiledev = np.array([[0,1,1,1,0,0,0],[1,0,0,0,1,0,0],[1,0,0,0,0,1,0],[1,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0]])

Ligne4 = np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]])

Ligne5 = np.array([[0,1,0,0,0],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,1],[0,0,0,1,0]])



#méthode par énumération:

#try all node combinations, see which ones cover all edges, out of those see the ones that are minimal.
def CPS_parfaite(a): #WARNING VERY LONG ALGORITHM dans pire des cas O(n!) ou n = nb nodes
    import itertools
    edges = getE(a)
    for s in range(len(a)+1):
        for i in itertools.permutations(a,s):
            bool=True
            for j in range(len(edges)):
                #print(i)
                if (edges[j][0] not in i) and (edges[j][1] not in i):
                    bool=False
                    break
            if not bool:
                continue
            return i,s

#fonction qui crée un index des villes avec des chiffres (utilisé pour la france)
def nbredges(a):
    index={}
    for i in range(len(a.getV)):
        index[a.getV()]=i
    for i in range(len(a.getE)):
        newedges=(index[a.getE[i][0]],index[a.getE[i][1]])
    return newedges


# glouton matrix
#algorithme glouton pour une matrice, seul pb elle résoud pour les vertices pas les edges :/
# matrices are kinda annoying anyways, I think we'll juste switch to adjacency lists for now.
#should do a matrix , list converter then

# bon en fait on a eu une meilleure idée en retirant les edges et ca marche mieux qu'avec les listes d'adjacence donc better.*
#cplx = O(n^4)
#O(n^2) now o(kn mieux)
def couvsommetmat(M,caméras=[]):
    import numpy as np
    import matplotlib.pyplot as plt
    #a=Graph(G)
    #M = a.Mat()
    Z = np.zeros(M.shape)
    max=0
    o=0
    cams=caméras
    I=np.sum(np.sum(M,1)) #ordre global
    while I!=0:
        max=0
        for i in range(M.shape[0]): #n
            u=np.sum(M,0)[i] #n
            if u >= max:
                max=u
                o=i
        for j in range(M.shape[0]): #n
            I-=2*M[o][j]
            M[o][j]=0
            M[j][o]=0
        cams.append(o)
    return cams

def printsolved(G,cams,coords=None):
    import networkx as nx
    g=nx.Graph(G)
    colormap=[]
    for nodes in g:
        if nodes in cams:
            colormap.append('red')
        else: colormap.append('blue')
    nx.draw(g, pos=coords, node_color=colormap)
    plt.show()

# optimisation

def culdesac(G):
    cams = []
    while 1 in alldeg(G) :
        Alldeg = alldeg(G)
        #print("Au départ :",Alldeg)
        for i in range(len(Alldeg)) :
            if Alldeg[i] == 1 :
                for j in range(len(G[i])):
                    if G[i][j] == 1 :
                        if j not in cams:
                            cams.append(j)
                        G[j][i] = 0
                        G[i][j] = 0

                        for k in range(len(G[j])): #Ici on fait ca pour empêcher de considérer les endroits avec cams comme cul de sac
                            G[j][k] = 0
                            G[k][j] = 0
                        #print("On ajoute en cams :",cams)
                #print("On a donc Alldeg =",Alldeg)

    return G ,cams # Renvoi le Graph original (préfère le graph réduit ?) et l'emplacement des caméras.

def solve_genral(graph):
    if isinstance(graph,dict):
         graph=Transfo_Dict_To_Mat(graph)
    copie= copy.deepcopy(graph)
    a,b = culdesac(copie)
    cams=couvsommetmat(a,b)
    printsolved(graph,cams)

# :::::::::::::::::::: PARTIE EXECUTION ::::::::::::::::::

solve_genral(lobster)

## fichier carte france
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

PATH0="C:\\Users\\Romai\\Documents\\L2\\Algorithmie & App\\projet\\"
f=open(PATH0+"france.gr","r",encoding="UTF-8")
L=f.readlines()
f.close()
G=[]

for i in range(len(L)):
    u=L[i].split(' ',4)
    G.append(u)


pos={}
index={}


Edges=[]
for i in range(len(G)):
    if G[i][0]=="v":
        u=G[i][1]
        v=(int(G[i][2]),1000-int(G[i][3][:-1]))
        pos[u]=v
        index[i]=G[i][1]
    else:
        u=G[i][1]
        v=G[i][2]
        Edges.append((u,v))

Nodes=pos.keys()

G=nx.Graph()
G.add_nodes_from(Nodes)
G.add_edges_from(Edges)

nx.draw(G,pos)
plt.show()
# code part
import copy

France = nx.to_dict_of_lists(G)
M = Transfo_Dict_To_Mat(France)
cams_nombres= couvsommetmat(M)
cams_villes=[]
for i in range(len(cams_nombres)):
    cams_villes.append(index[cams_nombres[i]])

printsolved(France,cams_villes,pos)




