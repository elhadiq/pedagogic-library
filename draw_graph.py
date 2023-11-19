import graphviz
import time
def root(A):
    if A!=[]:
        return str(A[0])
def left_child(A):
    if A!=[]:
        return A[1]
def right_child(A):
    if A!=[]:
        return A[2]
def is_empty(A):
    return A==[]
    
def draw_tree(A,title):
    #Parcour en largeur
    dot = graphviz.Digraph(title,comment='A binary tree',node_attr={'color': 'lightblue2', 'style': 'filled'})
    Tree_Dot=dict()#permet de donner une correpo,dance entre les nodes de A et les labels de Dot
    file=[(A,-1)]
    i=0
    while file!=[]:
        T,i_pere=file.pop(0)
        dot.node(str(i),str(root(T)))
        if i!=0:
            dot.edge(str(i_pere),str(i))
        Tree_Dot[root(T)]=i
        gauche=left_child(T)
        droit=right_child(T)
        if gauche!=[]:
            file.append((gauche,i)) 
        if droit!=[]:
            file.append((droit,i))
        i+=1
    dot.attr(label=title)
    dot.attr(fontsize='20')
    return dot,Tree_Dot

def animate_secuence(Tree,sequence,titel="a sequence"):
    dot,Tree_Dot=draw_tree(Tree,titel)
    dot.attr(label=titel)
    dot.attr(fontsize='20')
    yield dot
    sequence2=[]
    i=0
    while True:
        i=i%len(sequence)
        node=sequence[i]
        sequence2.append(node)
        #dot.node("#sequence#",titel+"\n=["+"\n".join(sequence2)+"]",shape="rectangle")
        dot.attr(label=titel+"=\n["+"  ".join(sequence[:i+1])+"]",shape="rectangle")
        dot.node(str(Tree_Dot[node]),color="red")
        yield dot
        dot.node(str(Tree_Dot[node]),color="lightblue")
        i+=1





def draw_graphe(ugraphe):
    dot = graphviz.Graph(comment='A binary tree',node_attr={'color': 'lightblue2', 'style': 'filled'})
    edges=[]
    for node in sorted(ugraphe):
        for adjacent in ugraphe[node]:
            if {node,adjacent} not in edges:
                edges.append({node,adjacent})
    for edge in [tuple(ed) for ed in edges]:
        dot.edge(edge[0],edge[1])
    return dot

def draw_digraphe(Digraph):
    dot = graphviz.Digraph(comment='A binary tree',node_attr={'color': 'lightblue2', 'style': 'filled'})
    for node in sorted(Digraph):
        for adjacent in Digraph[node]:
            dot.edge(node,adjacent)
    return dot

if __name__=="__main__":
    A=["+",["*",[4,[],[]],[5,[],[]]],["/",[6,[],[]],[7,[],[]]]]

    undirected_graphe={
    "A":["B","C"],
    "B":["A","D"],
    "C":[],
    "D":["B","A"]
}
    d=animate_secuence(A,["+",'*'],'a seq')
    for a in d:
        a.view()
        time.sleep(1)
