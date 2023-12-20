import heapq
class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.save_cost = None
        self.pr = []
        self.chld = []
    def __repr__(self):
        return str(dict({
            "label":self.label,
            "cost": self.cost,
            "goal cost": self.goal_cost
        }))
    def __eq__(self, other):
        return self.label == other.label
    def __lt__(self, other):
        if self.save_cost == 10000:
            return self.goal_cost + self.cost < other.goal_cost + other.cost
        else:
            return self.cost < other.cost

    def get_label(self):
        return self.label
    def neighbors(self):
        return self.chld + self.pr

class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)

    def add_node(self, node):
        self.nodes.append(node)

#Additional
    def get_node(self, label):
        for node in self.nodes:
            if node.label == label:
                return node
        return None

    def add_edges(self, edges):
        for edge in edges:
            node1 = self.get_node(edge[0])
            node2 = self.get_node(edge[1])
            cost = edge[2]
            self.edges.append((node1, node2, cost))
            node1.chld.append(node2)
            node2.pr.append(node1)
    
    def get_edge(self, node1, node2):
        for edge in self.edges:
            if edge[0] == node1 and edge[1] == node2:
                return edge
        return None
#Additional
    
def update_cost(tree, current_node, prev_node):
        if tree.get_edge(prev_node, current_node) is not None:
            if current_node.cost > prev_node.cost + tree.get_edge(prev_node, current_node)[2]:
                current_node.cost = prev_node.cost + tree.get_edge(prev_node, current_node)[2]
def A_Star(tree, start, end):
        frontier = [start]
        heapq.heapify(frontier)
        explored = []
        while len(frontier) > 0:
            state = heapq.heappop(frontier)
            explored.append(state)
            print(state)
            if state == end:
                return explored
            for child in state.neighbors():
                update_cost(tree,child,state)
                if child.get_label() not in list(set(node.get_label() for node in frontier + explored )):
                    heapq.heappush(frontier,child)
        return False
    
if __name__ == "__main__":
    tree = Tree()
    tree.add_nodes([
        Node("A",6),
        Node("B",3),
        Node("C",4),
        Node("D",5),
        Node("E",3),
        Node("F",1),
        Node("G",6),
        Node("H",2),
        Node("I",5),
        Node("J",4),
        Node("K",2),
        Node("L",0),
        Node("M",4),
        Node("N",0),
        Node("O",4)
    ])

    tree.add_edges([
        ("A", "B", 2),
        ("A", "C", 1),
        ("A", "D", 3),
        ("B", "E", 5),
        ("B", "F", 4),
        ("C", "G", 6),
        ("C", "H", 3),
        ("D", "I", 2),
        ("D", "J", 4),
        ("F", "K", 2),
        ("F", "L", 1),
        ("F", "M", 4),
        ("H", "N", 2),
        ("H", "O", 4)
    ])
    tree.nodes[0].cost = 0
    result = A_Star(tree, tree.nodes[0], tree.nodes[14])
    if result:
        s = 'explored: '
        for i in result:
            s+=i.label + " "
            print(s)
    else: 
        print("404 Not Found!")