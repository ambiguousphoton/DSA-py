from queue import Queue



graph = {
    "A":["B","D"],
    "B":["C","A"],
    "C":["B"],
    "D":["E","F","A"],
    "G":["H","E"],
    "H":["G","F"],
    "F":["E","H","D"],
    "E":["D","F","G"]
}

visited = {}
level = {}
parent = {}
bfs_traversal_output = [] 
queue  = Queue()

for node in graph.keys():
    visited[node] = False
    parent[node] = None
    level [node] = -1


s = 'A'
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

print (  "BFS OUTPUT :: " , " " , bfs_traversal_output)

print ("PARENT RELATIONS :: ",parent)
print ("LEVEL OF NODES :: ",level)
