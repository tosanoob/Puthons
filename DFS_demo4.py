def DFS(initialState, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(len(frontier) - 1)
        explored.append(state)
        if goal == state:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return False
if __name__ == "__main__":
    V = ["S", "A", "C", "B", "D", "F", "E", "H", "G"]
    E = [("S", "A"),
        ("S", "B"),
        ("S", "C"), 
        ("A", "B"),
        ("A", "D"),
        ("B", "D"),
        ("B", "C"), 
        ("B", "F"),
        ("B", "G"),
        ("C", "F"),
        ("E", "F"), 
        ("E", "G"),
        ("F", "H"),
        ("H", "G"),
        ("D", "E")
    ]

    graph = {v: [] for v in V}
    for e in E:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    path = DFS("S", "G")
    if path:
        s = 'explored: '
        for i in path:
            s += i + ' '
            print(s)
    else:
        print("Khong tim thay duong di")