from queue import PriorityQueue



nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}


def djikstra(graph,start):
    visited = set()
    minDistances = {}

    queue = PriorityQueue()
    minDistances[start] = 0
    queue.put((0, start))

    # LOOP UNTIL EVERY NODE IS EXPLORED
    while (not queue.empty()):
        currentNode = queue.get()
        currentNode = currentNode[1]
        if (currentNode not in visited):
            visited.add(currentNode)

            # EXPLORE THE NEIGHBOURS OF THE CURRENT NODE
            for [nextNode, distanceToNextNode] in graph[currentNode].items():
                currentWeight = minDistances[currentNode] + distanceToNextNode
                nextNodeMinDistance = minDistances.get(nextNode, "UNSET")

                # VISIT ONLY UNVISITED NODES + ONLY SET THE NODE MIN DISTANCE WHEN IT THE CURRENT IS LESS THAN THE RECORDED MINIMUM
                if (nextNode not in visited):
                    if (nextNodeMinDistance == "UNSET" or currentWeight<nextNodeMinDistance):
                        minDistances[nextNode] = currentWeight
                        queue.put((currentWeight, nextNode))

    return minDistances

print(djikstra(distances,"B"))


# O (V + E log V)