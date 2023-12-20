#tạo class Tree thủ công, lưu trữ một cây các node có trọng số, các cạnh không có trọng số
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

#without alpha & beta

def MaxValue(node, depth):
    print(node.get_data())
    if len(node.children) == 0 or depth == 0:
        return node
    node.value = -100000
    for child in node.children:
        temp = MinValue(child,depth-1)
        if temp.value > node.value:
            node.value = temp.value
    return node

def MinValue(node, depth):
    print(node.get_data())
    if len(node.children) == 0 or depth == 0:
        return node
    node.value = 100000
    for child in node.children:
        temp = MaxValue(child, depth-1)
        if temp.value < node.value:
            node.value = temp.value
    return node

def Minimax_Search(node, isMax = True, depth = 4):
    if isMax: 
        return MaxValue(node, depth)
    else:
        return MinValue(node, depth)

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

print(Minimax_Search(A,isMax=False).value)

# tree state:
#     A
#         B
#             D
#                 H 2
#                 I 9
#             E
#                 J 7
#                 K 4
#         C
#             F
#                 M 8
#                 N 9
#             G
#                 L 3
#                 Z 5