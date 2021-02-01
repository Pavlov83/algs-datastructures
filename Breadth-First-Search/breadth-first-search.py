from queue import Queue
'''
First step is to create a dictionary in which
every key holds as a value its adj. nodes 
'''

adj_list = {
    "A":["B", "D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}

'''
Next step is to create an empty dictionary which
will keep track of the visited nodes
'''
visited = {}

'''
Third Step is to create another dictionary with
the distance of each node from beginning
'''
level = {}

'''
The next should keep the parent of each node

'''
parent = {}

bfs_traversal_output = []

queue = Queue()

#we have to traverse trough all nodes in the list

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = 'A'
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)

print(bfs_traversal_output)
print(level['G'])

v = 'G'
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)
