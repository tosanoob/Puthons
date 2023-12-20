class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    def addChild(self, list):
        for c in list:
            self.children.append(c)

def DFS(initialState, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop()
        explored.append(state)
        if goal == state.name:
            return explored
        for child in state.children:
            if child not in (explored and frontier):
                frontier.append(child)
    return False

if __name__ == '__main__':
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    nodeI = Node("I")
    nodeJ = Node("J")
    nodeK = Node("K")
    nodeL = Node("L")
    nodeM = Node("M")
    nodeN = Node("N")
    nodeO = Node("O")
    nodeA.addChild([nodeB, nodeC])
    nodeB.addChild([nodeD, nodeE])
    nodeC.addChild([nodeF, nodeG])
    nodeD.addChild([nodeH, nodeI])
    nodeE.addChild([nodeJ, nodeK])
    nodeF.addChild([nodeL, nodeM])
    nodeG.addChild([nodeN, nodeO])
    result = DFS(nodeA, 'H')
    if result:
        s = 'explored: '
        for i in result:
            s += i.name + " "
            print(s)
    else:
        print("404 Not Found!")
    