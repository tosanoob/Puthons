def BFS(initialState, goal):
    #list frontier lưu các trạng thái biên, list explored lưu các trạng thái đã khám phá
    #trạng thái = node của graph
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(0)
        #kiểu queue: append đuôi, pop đầu
        #kiểu stack: append đuôi, pop đuôi
        explored.append(state)
        if goal == state:
            #nếu trạng thái đang tìm khớp goal thì trả
            return explored
        
        #graph[state] trả về 'value' của record có 'key' = state
        #neighbor duyệt tập node con của nó
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                #nếu neighbor chưa có trong explored và frontier => thêm vào đuôi frontier
                frontier.append(neighbor)
    #duyệt hết, không tìm thấy => trả về False
    return False

def DFS(initialState, goal):
    #list frontier lưu các trạng thái biên, list explored lưu các trạng thái đã khám phá
    #trạng thái = node của graph
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(-1)
        #kiểu queue: append đuôi, pop đầu
        #kiểu stack: append đuôi, pop đuôi
        explored.append(state)
        if goal == state:
            #nếu trạng thái đang tìm khớp goal thì trả
            return explored
        
        #graph[state] trả về 'value' của record có 'key' = state
        #neighbor duyệt tập node con của nó
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                #nếu neighbor chưa có trong explored và frontier => thêm vào đuôi frontier
                frontier.append(neighbor)
    #duyệt hết, không tìm thấy => trả về False
    return False


if __name__ == '__main__':
    
    #cây trạng thái là một dictionary, khai báo theo 'key' - 'value'
    #trong đó 'key' là tên node, 'value' là các node con của nó
    graph = {
        'A' : ['B','C'],
        'B' : ['D','E'],
        'C' : ['F','G'],
        'D' : ['H','I'],
        'E' : ['J','K'],
        'F' : ['L','M'],
        'G' : ['N','O'],
        'H' : [],
        'I' : [],
        'J' : [],
        'K' : [],
        'L' : [],
        'M' : [],
        'N' : [],
        'O' : []
    }
    #print(type(graph)) => class'dict'

    result = DFS('A','O')
    if result:
        s = 'explored: '
        for i in result:
            s+= i + ' '
            print(s)
    else: print("Not found")