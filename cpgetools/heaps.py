import graphviz


def draw_heap1(L,title):
    #Parcour en largeur
    dot = graphviz.Digraph("aa",comment='A binary tree',node_attr={'color': '#FFB6C1', 'style': 'filled'})
    Tree_Dot=dict()#permet de donner une correpo,dance entre les nodes de A et les labels de Dot
    for i in range(len(L)):
        dot.node(str(i),str(L[i]))
    for i in range((len(L))//2):
        dot.edge(str(i),str(2*i+1))
        if 2*i+2<len(L):
            dot.edge(str(i),str(2*i+2))
    dot.attr(label="\n\n"+title)
    dot.attr(fontsize='20')
    return dot,Tree_Dot

def draw_heap(L,title="Heap"):
    return draw_heap1(L,title)[0]

def draw_tab(L):
    s = graphviz.Digraph('aa', filename='aa.gv',
                        node_attr={'shape': 'record'})
    s.node('tab','|'.join(['<L'+str(i)+'>'+str(L[i]) for i in range(len(L))]))
    for i in range((len(L))//2):
        s.edge('tab:L'+str(i), 'tab:L'+str(2*i+1))
        if 2*i+2<len(L):
            s.edge('tab:L'+str(i), 'tab:L'+str(2*i+2))
    return s


pere=lambda i:(i-1)//2
gauche=lambda i:2*i+1
droite=lambda i:2*(i+1)

def percolation(T,inode,limit=None):
    if limit is None:
        limit=len(T)
    if inode <=(limit-1)//2:
        if gauche(inode)<limit:
            imax=inode if T[inode]>=T[gauche(inode)] else gauche(inode)
            if droite(inode)<limit:
                imax=imax if T[imax]>=T[droite(inode)] else droite(inode)
            if inode!=imax:
                T[inode],T[imax]=T[imax],T[inode]
                percolation(T,imax,limit)

def construireTas(T):
    for i in range(len(T)//2,-1,-1):
        percolation(T,i)

def tri_tas(T):
    construireTas(T)
    for longeur in range(len(T)-1,0,-1):
        T[longeur],T[0]=T[0],T[longeur]
        percolation(T,0,longeur)

def percolation1(T,inode,limit=None):
    if limit is None:
        limit=len(T)
    if inode <=(limit-1)//2:
        if gauche(inode)<limit:
            imax=inode if T[inode]>=T[gauche(inode)] else gauche(inode)
            if droite(inode)<limit:
                imax=imax if T[imax]>=T[droite(inode)] else droite(inode)
            if inode!=imax:
                T[inode],T[imax]=T[imax],T[inode]
                yield 
                percolation1(T,imax,limit)

def construireTas1(T):
    for i in range(len(T)//2,-1,-1):
         percolation1(T,i)
         yield