# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

# QUEUE
def bfs(graph, start):
    queue = [start]
    while (len(queue) > 0):
        # GETS FIRST ITEM
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbour in graph[node]:
                queue.append(neighbour)

bfs(graph,"A")