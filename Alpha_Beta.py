# from TreeNode import Tree
def MaxValue(node, alpha, beta):
    if len(node.children) == 0:
        return node
    node.value = -100000
    for child in node.children:
        temp = MinValue(child, alpha, beta)
        if temp.value >node.value:
           node.value = temp.value
        if child.value >= beta:
            return child
        if child.value > alpha:
            alpha = child.value
    return node

def MinValue(node, alpha, beta):
    #nếu node là node lá => trả về chính nó
    if len(node.children) == 0:
        return node
    #khởi tạo 'min' ban đầu là lớn vô cùng
    node.value = 100000
    
    #duyệt qua từng node con, lấy Max từng cây con của node đó
    for child in node.children:
        temp = MaxValue(child, alpha, beta) #node là min, do đó duyệt max từ các con
        #nếu temp<node => gán node là min giá trị của cây con của chính nó
        if temp.value < node.value:
            node.value = temp.value 
        
        #alpha là max trong các đỉnh con của tầng max 
        #nếu một child nào đó <= alpha => chắc chắn sẽ không được chọn, không ảnh hưởng tới alpha => cắt tỉa, trả về child
        if child.value <= alpha:
            return child
        #beta là min trong các đỉnh con của tầng min
        #nếu một child < beta => cập nhật beta mới
        if child.value < beta:
            beta = child.value
    #lấy node là min của các nút con
    return node

def Alpha_Beta_Search(state):
    MinValue(state, -100000,100000)
    
class Tree:
    def __init__(self, data, cost = 100000):
        self.data = data
        self.cost = cost
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_data(self):
        return self.data
    def get_children(self):
        return self.children
    def __lt__(self,other):
        return self.cost < other.cost

if __name__=="__main__":
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    J = Tree("J")
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
    
# A min BC max DEFG min => {2,4,8,3} => {4,8} => {4}
Alpha_Beta_Search(A)
print(A.value)