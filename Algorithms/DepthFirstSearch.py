# Complexity:  O(V + E)

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

#  STACK / RECURSIVE STACK
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')

# Using Adjacency matrix
adjacencyMatrix = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
    ]

visited = set()

def dfs(visited, adjacencyMatrix, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbourIndex in range(len(adjacencyMatrix[node])):
            weight = adjacencyMatrix[node][neighbourIndex]
            if (weight):
                dfs(visited,adjacencyMatrix,neighbourIndex)

dfs(visited,adjacencyMatrix,0)
