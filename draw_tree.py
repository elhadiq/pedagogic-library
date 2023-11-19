import graphviz
def root(A):
    if A!=[]:
        return A[0]
def left_child(A):
    if A!=[]:
        return A[1]
def right_child(A):
    if A!=[]:
        return A[2]
    
def draw_tree(A):
    #Parcour en largeur
    dot = graphviz.Digraph(comment='A binary tree')
    file=[(A,-1)]
    i=0
    while file!=[]:
        T,i_pere=file.pop(0)
        dot.node(str(i),str(root(T)))
        if i!=0:
            dot.edge(str(i_pere),str(i))
        gauche=left_child(T)
        droit=right_child(T)
        if gauche!=[]:
            file.append((gauche,i)) 
        if droit!=[]:
            file.append((droit,i))
        i+=1
    if __name__=="__main__":
        dot.render('Digraph.gv',view=True)
        print("hi")
    return dot
if __name__=="__main__":
    A=["+",["*",[4,[],[]],[5,[],[]]],["/",[6,[],[]],[7,[],[]]]]
    graph=draw_tree(A)
    print("hi")