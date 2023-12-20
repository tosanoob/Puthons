class Tree:
    def __init__(self, data, cost = 100000):
        self.data = data
        self.cost = cost
        self.children = []
        self.parent = None
        self.value = 0

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def get_data(self):
        return self.data
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def __lt__(self, other):
        return self.cost < other.cost

#with alpha&beta:
#alpha: max trong các đỉnh con của tầng max
#beta: min trong các đỉnh con của tầng min
def MaxValueAB(node, alpha, beta, depth):
    print(node.get_data())
    if len(node.children) == 0 or depth == 0:
        return node
    node.value = -100000
    for child in node.children:
        temp = MinValueAB(child, alpha, beta, depth-1)
        if temp.value > node.value:
            node.value = temp.value
        if child.value >= beta:
            return child
        if child.value > alpha:
            alpha = child.value
    return node

def MinValueAB(node, alpha, beta, depth):
    print(node.get_data())
    if len(node.children) == 0 or depth == 0:
        return node
    node.value = 100000
    for child in node.children:
        temp = MaxValueAB(child, alpha, beta, depth-1)
        if temp.value < node.value:
            node.value = temp.value
        if child.value < beta:
            beta = child.value
        if child.value <= alpha:
            return child
    return node

def Minimax_SearchAB(node, isMax = True, depth = 4):
    if isMax: 
        return MaxValueAB(node, -100000, 100000, depth)
    else:
        return MinValueAB(node, -100000, 100000, depth)

if __name__ == "__main__":
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)
    C.add_child(G)
    D.add_child(H)
    D.add_child(I)
    E.add_child(J)
    E.add_child(K)
    F.add_child(M)
    F.add_child(N)
    G.add_child(L)
    G.add_child(Z)
    H.value = 2
    I.value = 9
    J.value = 7
    K.value = 4
    M.value = 8
    N.value = 9
    L.value = 3
    Z.value = 5

print(Minimax_SearchAB(A,isMax=False).value)

# tree state:
#     A min = 4
#         B max = 4
#             D min = 2
#                 H 2
#                 I 9
#             E min = 4
#                 J 7
#                 K 4
#         C max = 8
#             F min = 8
#                 M 8
#                 N 9
#             G min = 3
#                 L 3
#                 Z 5