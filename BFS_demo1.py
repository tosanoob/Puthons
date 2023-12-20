def BFS(initialState, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(0)
        explored.append(state)
        if goal == state:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return False


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

result = BFS('G', 'S')
if result:
    s = 'explored: '
    for i in result:
        s += i + ' '
        print(s)
else:
    print("404 Not found!")
