# archive générale de codes inutilisés




##ancienne classe de graphs basée sur des dicts de listes (dict d'adjacence)
class Graph():
    #graph composed of vertices and edges, should build getV and getE f, then add V, add E, and print graph (raw data, will be used for extension)
    #{a:[e,g],b:[f,i],i:[b,o]}
    def __init__(self,dict={}):
        if dict == None:
            self.gdict={}
        else :
            self.gdict=dict
    def getV(self):
        return list(self.gdict.keys())
    def getE(self):
        u=[]
        for i in list(self.gdict.keys()):
            for j in self.gdict[i]:
                if (i,j) and (j,i) not in u:
                    u.append((i,j))
        return u
    def addV(self,a):
        if a not in self.gdict:
            self.gdict[a]=[]
        else:
            print("Vertex already exists")
    def addE(self,t):
        if t[1] not in self.gdict[t[0]]:
            self.gdict[t[0]].append(t[1])
            self.gdict[t[1]].append(t[0])
        else:
            print("Edge already exists")
    def deg(self,a):
        return len(self.gdict[a])
    def Mat(self):
        import numpy as np
        L=list(self.gdict)
        o=len(L)
        M=np.zeros((o,o))
        for i in range(len(L)):
            for j in range(len(L)):
                if L[i] in self.gdict[L[j]]:
                    M[i][j]=1
        return M

##anciennce résolution a partir de dicts de listes (incomplete)
# algo glouton 1 [REDACTED]
# given up as annoying to remove all nodes, when not all edges covered and no nodes left
import networkx as nx
import matplotlib.pyplot as plt
import copy
a=Graph(lobster)

cams=[]
couverts=[]
Gra=copy.deepcopy(a.gdict)
Gra2=copy.deepcopy(a.gdict)
while len(couverts)!=len(a.getE()): #n mettre tantque rest!={}
    if Gra=={}:
        reste=[i for i in a.getE() if i not in couverts] #faire a l'exterieur avec A.getEdge()
        print("00000",reste)
        v=list(Gra2.keys())[0]
        if Gra2[v] not in cams:
            cams.append(v)
            for u in Gra2.pop(v):
                if (u,v) not in couverts:
                    if (v,u) not in couverts:
                        couverts.append((u,v))
        else: Gra2.pop(v)
    else:
        maxlen=0
        o=0
        for i in Gra: #n
            if len(Gra[i])>=maxlen:
                maxlen=len(Gra[i])
                o=i
        cams.append(o)
        for u in Gra.pop(o): #k edges of nth
            if u in Gra:
                Gra.pop(u)
            if (u,o) not in couverts:
                if (o,u) not in couverts:
                    couverts.append((o,u))
print("installer des caméras à",cams)
g=nx.Graph(lobster)
colormap=[]
for nodes in g:
    if nodes in cams:
        colormap.append('red')
    else: colormap.append('blue')
nx.draw(g,node_color=colormap)
plt.show()

### Classe de graphs basée sur les listes de listes (matrice d'adjacence)

import numpy as np

class Graph:

    def __init__(self,G = np.array([])):
        self.g = G
        self._numV = len(self.g)

    def __str__(self):
        return str(self.g)

    def getV(self):
        tab = []
        for i in range(len(self.g)):
            tab += (i,self.g[i])
        return tab

    def getE(self):
        tab = []
        self._numE = 0
        n = len(self.g)
        for i in range(n):
            for j in range(n-i):
                if self.g[i][n-j] == 1:
                    self._numE += 1
                    tab += (i,j)
        return tab

    def addV(self):
        self.g.append([0]*self._numV)
        for t in self.g:
            t.append(0)
        self._numV += 1

    def addE(self,i,j):
        if i == j:
            print("Cannot add an edge between a vertice and itself")
        elif (0 <= i <= self._numV - 1) and (0 <= j <= self._numV - 1):
            if self.g[i][j] == 0:
                self.g[i][j] = 1
                self.g[j][i] = 1
            else:
                print("Edge already exists")
        else :
            print(f"index out of range, not belonging to [0,{self._numV -1}]")

    def removeE(self,i,j):
        if (0 <= i <= self._numV - 1) and (0 <= j <= self._numV - 1):
            if self.g[i][j] == 1:
                self.g[i][j] = 0
                self.g[j][i] = 0
            else:
                print("Edge doesn't exists")
        else :
            print(f"index out of range, not belonging to [0,{self._numV-1}]")

    def removeV(self,i):
        if (0 <= i <= self._numV - 1):
            self.g.pop(i)
            for j in range(self._numV-1):
                for k in range (i,self._numV-1):
                    self.g[j][k] = self.g[j][k+1]
                self.g[j].pop(self._numV-1)
            self._numV -= 1
        else:
            print("Vertice doesn't exists")

    def deg(self,i):
        deg = 0
        for j in self.g[i]:
            deg += j


## interface plus complexe mais non terminée

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter.ttk as ttk

saved_graphs = ["Choose here", "test1",2,3]

G = Graph()

def prelaunch_interface():
    window = tk.Tk()
    window.title("Screen resolution")
    label = tk.Label(window, text = "Which resolution do you want?", font = ("Arial",10))
    label.grid(column = 0, row = 0)
    def clicked1():
        window.destroy()
        return launch_interface((720,480))
    def clicked2():
        window.destroy()
        return launch_interface((1280,720))
    def clicked3():
        window.destroy()
        return launch_interface((1920,1080))
    btn1 = tk.Button(window, text = "480p", command = clicked1)
    btn2 = tk.Button(window, text = "720p", command = clicked2)
    btn3 = tk.Button(window, text = "1080p", command = clicked3)
    btn1.grid(column = 1, row = 0)
    btn2.grid(column = 2, row = 0)
    btn3.grid(column = 3, row = 0)
    window.mainloop()

def launch_interface(res):
    window = tk.Tk()
    window.title("Graph Interface")
    window.geometry("{}x{}".format(res[0],res[1]))
    label1 = tk.Label(window, text = "Which way do you want to enter your graph?", font = ("Arial",res[0]//100), padx = res[0]//3, pady = res[1]//20)
    label2 = tk.Label(window, text = "Warning, multiple graphs must not be entered.", font = ("Arial",res[0]//100), padx = 0, pady = res[1]//30)
    label1.grid(column = 0, row = 0, columnspan = 4)
    label2.grid(column = 0, row = 1, columnspan = 4)
    def clicked1():
        window.destroy()
        return text_interface(res, True)
    def clicked2():
        window.destroy()
        return text_interface(res, False)
    def clicked3():
        window.destroy()
        return draw_graph((1280,720))
    def clicked4():
        window.destroy()
        return saved_interface(res)
    btn1 = tk.Button(window, text = "add a dictionnary\nimplemented graph", command = clicked1, padx = 0 )
    btn2 = tk.Button(window, text = "add an adjacency matrix", command = clicked2, padx = 0)
    btn3 = tk.Button(window, text = "draw the graph", command = clicked3, padx = 0)
    btn4 = tk.Button(window, text = "select a local graph", command = clicked4, padx = 0)
    btn1.grid(column = 0, row = 2)
    btn2.grid(column = 1, row = 2)
    btn3.grid(column =2, row = 2)
    btn4.grid(column = 3, row = 2)
    window.mainloop()

def text_interface(res, b):
    window = tk.Tk()
    window.title("Graph typing")
    window.geometry("{}x{}".format(res[0],res[1]))
    if b :
       label = tk.Label(window, text = "Enter your graph as a dict:", padx = res[0]//100)
    else :
       label = tk.Label(window, text = "Enter your graph as a numpy array:", padx = res[0]//100)
    label.grid(column = 0, row = 0)
    txt = scrolledtext.ScrolledText(window, width = 100, height = 20)
    txt.grid(column = 0, row = 1)
    def save_button():
        inp = txt.get(1.0, "end-1c")
        window.destroy()
        return inp
    def clear_button():
        txt.delete(1.0,"end-1c")
    cl_bt = tk.Button(window, text = "Clear All", font = ("Arial", 10,"bold"), padx = 15, pady = 15, command = clear_button)
    sv_bt = tk.Button(window, text = "Save", font = ("Arial", 10, "bold"), padx = 15, pady = 15, command = save_button)
    sv_bt.grid(column = 1, row = 2)
    cl_bt.grid(column = 0, row = 2)
    window.mainloop()

def saved_interface(res):
    root = tk.Tk()
    root.title("Saved Graphs")
    root.geometry("{}x{}".format(res[0],res[1]))
    label = tk.Label(root, text = "Choose your graph :", font = ("Arial",20))
    label.pack(expand = tk.YES)
    combo = ttk.Combobox(root, font = ("Arial", 10, "bold"))
    combo["values"] = saved_graphs
    combo.current(0)
    combo.pack()
    def save_button():
        inp = combo.get()
        root.destroy()
        return inp
    sv_bt = tk.Button(root, text = "Save", font = ("Arial", 15, "bold"), command = save_button)
    sv_bt.pack(expand = tk.YES)
    root.mainloop

def draw_graph(res):

#     Fenetre principale :

    root = tk.Tk()
    root.title("Draw your Graph")
    root.geometry("{}x{}".format(res[0],res[1]))
    label = tk.Label(root, text = "Select vertexes :", font = ("Arial",15))
    label.pack()

#  Découpage de la fenetre

    Frame0 = tk.Frame(root, bg = "snow", height = res[1], width = res[0]//15)
    Frame0_5 = tk.Frame(root, bg = "snow", height = res[1], width = (2*res[0])//5)
    Frame1 = tk.Frame(root, bg = "snow", height = res[1], width = res[0]//15)
    Frame1_5 = tk.Frame(root, bg = "snow", height = res[1], width = (2*res[0])//5)
    Frame2 = tk.Frame(root, bg = "snow", height = res[1], width = res[0]//15)
    Frame0.pack(side = tk.LEFT)
    Frame0_5.pack(side = tk.LEFT)
    Frame1.pack(side = tk.LEFT)
    Frame1_5.pack(side = tk.LEFT)
    Frame2.pack(side = tk.LEFT)

#     Listes pour stocker les sommets et arêtes selectionnées

    tab_V = []
    tab_E = []

    # On definit la premiere colonne avec des sommets :
    def bt_v1():
        v1.config(bg = "red2")
        tab_V.append("v1")
    def bt_v2():
        v2.config(bg = "red2")
        tab_V.append("v2")
    def bt_v3():
        v3.config(bg = "red2")
        tab_V.append("v3")
    def bt_v4():
        v4.config(bg = "red2")
        tab_V.append("v4")
    def bt_v5():
        v5.config(bg = "red2")
        tab_V.append("v5")
    def bt_v6():
        v6.config(bg = "red2")
        tab_V.append("v6")
    def bt_v7():
        v7.config(bg = "red2")
        tab_V.append("v7")
    def bt_v8():
        v8.config(bg = "red2")
        tab_V.append("v8")
    def bt_v9():
        v9.config(bg = "red2")
        tab_V.append("v9")
    def bt_v1_v2():
        v1_v2.config(bg = "lime green")
        tab_E.append("v1_v2")
    def bt_v2_v3():
        v2_v3.config(bg = "lime green")
        tab_E.append("v2_v3")
    def bt_v1_v4():
        v1_v4.config(bg = "lime green")
        tab_E.append("v1_v4")
    def bt_v2_v5():
        v2_v5.config(bg = "lime green")
        tab_E.append("v2_v5")
    def bt_v3_v6():
        v3_v6.config(bg = "lime green")
        tab_E.append("v3_v6")
    def bt_v4_v5():
        v4_v5.config(bg = "lime green")
        tab_E.append("v4_v5")
    def bt_v5_v6():
        v5_v6.config(bg = "lime green")
        tab_E.append("v5_v6")
    def bt_v4_v7():
        v4_v7.config(bg = "lime green")
        tab_E.append("v4_v7")
    def bt_v5_v8():
        v5_v8.config(bg = "lime green")
        tab_E.append("v5_v8")
    def bt_v6_v9():
        v6_v9.config(bg = "lime green")
        tab_E.append("v6_v9")
    def bt_v7_v8():
        v7_v8.config(bg = "lime green")
        tab_E.append("v7_v8")
    def bt_v8_v9():
        v8_v9.config(bg = "lime green")
        tab_E.append("v8_v9")

    v1 = tk.Button(Frame0, bg = "saddle brown", padx = 24, pady = 6, command = bt_v1)
    v1_v4 = tk.Button(Frame0, bg = "gray80", padx = 15, pady = 100, command = bt_v1_v4, state = "disabled")
    v4 =tk.Button(Frame0, bg = "saddle brown", padx = 24, pady = 6, command = bt_v4)
    v4_v7 = tk.Button(Frame0, bg = "gray80", padx = 15, pady = 100, command = bt_v4_v7, state = "disabled")
    v7 =tk.Button(Frame0, bg = "saddle brown", padx = 24, pady = 6, command = bt_v7)
    v1.pack()
    v1_v4.pack()
    v4.pack()
    v4_v7.pack()
    v7.pack()

    # puis la seconde :
    v2 = tk.Button(Frame1, bg = "saddle brown", padx = 24, pady = 6, command = bt_v2)
    v2_v5 = tk.Button(Frame1, bg = "gray80", padx = 15, pady = 100, command = bt_v2_v5, state = "disabled")
    v5 =tk.Button(Frame1, bg = "saddle brown", padx = 24, pady = 6, command = bt_v5)
    v5_v8 = tk.Button(Frame1, bg = "gray80", padx = 15, pady = 100, command = bt_v5_v8, state = "disabled")
    v8 =tk.Button(Frame1, bg = "saddle brown", padx = 24, pady = 6, command = bt_v8)
    v2.pack()
    v2_v5.pack()
    v5.pack()
    v5_v8.pack()
    v8.pack()

    # et la troisieme:
    v3 = tk.Button(Frame2, bg = "saddle brown", padx = 24, pady = 6, command = bt_v3)
    v3_v6 = tk.Button(Frame2, bg = "gray80", padx = 15, pady = 100, command = bt_v3_v6, state = "disabled")
    v6 =tk.Button(Frame2, bg = "saddle brown", padx = 24, pady = 6, command = bt_v6)
    v6_v9 = tk.Button(Frame2, bg = "gray80", padx = 15, pady = 100, command = bt_v6_v9, state = "disabled")
    v9 =tk.Button(Frame2, bg = "saddle brown", padx = 24, pady = 6, command = bt_v9)
    v3.pack()
    v3_v6.pack()
    v6.pack()
    v6_v9.pack()
    v9.pack()

    # On passe maintenant aux deux colonne d'edges:
    # la premiere:

    v1_v2 = tk.Button(Frame0_5, bg = "gray80", command = bt_v1_v2, state = "disabled")
    canvas1 = tk.Canvas(Frame0_5, bg = "snow", height = (38*res[1])//113)
    v4_v5 = tk.Button(Frame0_5, bg = "gray80", command = bt_v4_v5, state = "disabled")
    canvas2 = tk.Canvas(Frame0_5, bg = "snow", height = (38 *res[1])/113)
    v7_v8 = tk.Button(Frame0_5, bg = "gray80", command = bt_v7_v8, state = "disabled")
    v1_v2.pack(fill = tk.X)
    canvas1.pack()
    v4_v5.pack(fill = tk.X)
    canvas2.pack()
    v7_v8.pack(fill = tk.X)

    # la seconde:

    v2_v3 = tk.Button(Frame1_5, bg = "gray80", command = bt_v2_v3, state = "disabled")
    canvas3 = tk.Canvas(Frame1_5, bg = "snow", height = (38*res[1])//113)
    v5_v6 = tk.Button(Frame1_5, bg = "gray80", command = bt_v5_v6, state = "disabled")
    canvas4 = tk.Canvas(Frame1_5, bg = "snow", height = (38 *res[1])/113)
    v8_v9 = tk.Button(Frame1_5, bg = "gray80", command = bt_v8_v9, state = "disabled")
    v2_v3.pack(fill = tk.X)
    canvas3.pack()
    v5_v6.pack(fill = tk.X)
    canvas4.pack()
    v8_v9.pack(fill = tk.X)

    #     Dictionnaires permettant le lien entre "nom de variable" et variable (et une liste pour l'ordre).

    V_names = [ "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", ]
    dict_V = { "v1" : v1, "v2" : v2, "v3" : v3, "v4" : v4, "v5" : v5, "v6" : v6, "v7" : v7, "v8" : v8, "v9" : v9 }
    dict_E = { "v1_v2" : v1_v2, "v2_v3" : v2_v3, "v1_v4" : v1_v4, "v2_v5" : v2_v5, "v3_v6" : v3_v6, "v4_v5" : v4_v5,
    "v5_v6" : v5_v6, "v4_v7" : v4_v7, "v5_v8" : v5_v8, "v6_v9" : v6_v9, "v7_v8" : v7_v8, "v8_v9" : v8_v9 }

# index sert à référencer les sommets dans le graph

    index = {}

    def next_button():

#       On updates les boutons de sommets et on définit les arêtes concernées, en plus de débuter la création du graph

        potential_E = []
        cpt_v = 0

        for i in range(1,10):
            Vi = "v"+str(i)
            dict_V[Vi].config(state = "disabled")
            if Vi not in tab_V :
                dict_V[Vi].config(bg = "gray80")
            else :
                index[i] = cpt_v
                G.addV()
                cpt_v += 1
                if i in [1,2,4,5]:
                    if ("v"+str(i+1)) in tab_V:
                        potential_E.append(Vi + f"_v{i+1}")
                    if ("v"+str(i+3)) in tab_V:
                        potential_E.append(Vi + f"_v{i+3}")
                elif (i in [3,6]) and (("v"+str(i+3)) in tab_V):
                    potential_E.append(Vi + f"_v{i+3}")
                elif (i in [7,8]) and (("v"+str(i+1)) in tab_V):
                    potential_E.append(Vi + f"_v{i+1}")

#         Puis ceux des arêtes concernées

        for Ei in potential_E:
            dict_E[Ei].config(state = "normal", bg = "DarkGoldenrod2")

#         On update le bouton de sauvegarde

        sv_bt.config(text = "Save", command = save_button)

    def save_button():
        for i in range (1,10):
            for j in range(i+1,10):
                Eij = f"v{i}_v{j}"
                if Eij in tab_E :
                    G.addE(index[i], index[j])
        root.destroy()
        return G

    def clear_button():
        root.destroy()
        return  draw_graph(res)

    cl_bt = tk.Button(root, text = "Clear All", font = ("Arial", 10,"bold"), padx = 15, pady = 15, command = clear_button)
    sv_bt = tk.Button(root, text = "Next", font = ("Arial", 10, "bold"), padx = 15, pady = 15, command = next_button)
    sv_bt.pack(side = tk.BOTTOM)
    cl_bt.pack(side = tk.BOTTOM)

    root.mainloop

# Petit code initiatique à tkinter pour se parler à soi-même

import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)

# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
                        text = "Print",
                        command = printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()