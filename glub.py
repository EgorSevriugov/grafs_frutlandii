import networkx as nx
import matplotlib.pyplot as plt

def graf():
    N = int(input("Введите количество вершин: "))
    M = int(input("Введите количество рёбер: "))
    g = {}
    for i in range(N):
        g[str(i)] = {}
    for i in range(M):
        a,b,weight = input("Введите ребро через вершины с весом: ").split()
        g[a][b] = weight
    return(g)

def enter():
    func = input("Введите функцию: ")
    if func == "DFS":
        a,b = DFS()
    elif func == "BFS":
        a,b,c = BFS(input("Введите стаpтовую вершину: "),graf())
    elif func == "KS":
        komp_sviaz(input("Введите стартовую вершину: "),graf())
    if a:
        draws(a,b)

def DFS():
    mat = graf()
    start = input("Введите стартовую вершину: ")
    fired = []
    list = []
    g = nx.Graph()
    G,ls = recur(mat,start,fired,list,g)
    return g,ls

def BFS(start,mat):
    queue = [start]
    fired = [start]
    list = []
    g = nx.Graph()
    while queue:
        star = queue.pop(0)
        for neibours in mat[star]:
            if neibours not in fired:
                queue.append(neibours)
                fired.append(neibours)
                g.add_edge(star,neibours)
                list.append((star,neibours))
    return g,list,mat

def komp_sviaz(start,mat):
    g,ls,G = BFS(start,mat)
    lsG = [(g,ls)]
    if len(g) < len(G):
        for x in G:
            for y in range(len(lsG)):
                if x in lsG[y][0]:
                    break
            else:
                a,b,c = BFS(x,mat)
                lsG.append((a,b))
    drawss(lsG)
def draws(G,listed):
    listn = []
    pos = nx.spring_layout(G)
    for i in G:
        listn.append(i)
    nx.draw_networkx_nodes(G,pos,nodelist=listn,node_color='b',node_size=200,alpha=0.8)
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    nx.draw_networkx_edges(G,pos,edgelist=listed,width=2,alpha=0.5,edge_color='r')
    nx.draw_networkx_labels(G,pos,font_size=16)
    plt.axis('off')
    plt.savefig("labels_and_colors.png")
    plt.show()
def drawss(lsG):
    for x in range(len(lsG)):
        listn = []
        pos = nx.spring_layout(lsG[x][0])
        for i in lsG[x][0]:
            listn.append(i)
        nx.draw_networkx_nodes(lsG[x][0],pos,nodelist=listn,node_color='b',node_size=200,alpha=0.8)
        nx.draw_networkx_edges(lsG[x][0],pos,width=1.0,alpha=0.5)
        nx.draw_networkx_edges(lsG[x][0],pos,edgelist=lsG[x][1],width=2,alpha=0.5,edge_color='r')
        nx.draw_networkx_labels(lsG[x][0],pos,font_size=16)
    plt.axis('off')
    plt.savefig("labels_and_colors.png")
    plt.show()

def recur(G,start,f,list,g):
    f.append(start)
    for neibours in G[start]:
        if neibours not in f:
            list.append((start,neibours))
            g.add_edge(start,neibours)
            recur(G,neibours,f,list,g)
    return g,list

enter()