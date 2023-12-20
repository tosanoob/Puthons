from collections import deque

if __name__ == '__main__':
    V = ["S","A","B","C","D","E","F","G","H"]
    E = [ ("S","A"),
        ("S","B"),
        ("S","C"),
        ("A","B"),
        ("A","D"),
        ("B","C"),
        ("B","D"),
        ("B","F"),
        ("B","G"),
        ("C","F"),
        ("D","E"),
        ("E","F"),
        ("E","G"),
        ("F","H"),
        ("H","G")
        ]

graph = {v: [] for v in V}
for e in E:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])


def BFS(start, goal):
    queue = deque([(start, [start])])
    explored = set()

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return explored

        explored.add(node)

        for neighbor in graph[node]:
            if neighbor not in explored:
                queue.append((neighbor, path + [neighbor]))

    return None

def DFS(start, goal):
    explored = set();
    stack = deque([(start),[start]])

    while stack: 
        node, path = stack.pop(len(stack)-1)
        if node == goal:
            return explored
        
        explored.add(node)
        for neighbor in graph[node]:
            if neighbor not in explored:
                stack.append((neighbor, path + [neighbor]))

    return None

path = DFS("S", "G")

if path: 
    s = 'explored: '
    for i in path:
        s += i + ' '
        print(s)
else:
    print("Khong tim thay")

