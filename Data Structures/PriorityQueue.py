from queue import PriorityQueue

q = PriorityQueue()

#Putting More Items
q.put((4, 'Read'))
q.put((2, 'Play'))
q.put((5, 'Write'))
q.put((1, 'Code'))
q.put((3, 'Study'))

# Iterations
while not q.empty():
    next_item = q.get()
    print(next_item)


# This is a Heap/Priority Queue:
# Complexities:
#   Insertion:      O (log n)
#   Deletion:       O (log n)
#   Pop/Get Item:   O(1)