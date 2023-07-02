import random
# nodes  
def genrate(no_of_nodes: int, maxedges: int) -> dict:
    graph = dict()
    for node in range(no_of_nodes):
        graph[node] = [node]
        neighbours = {node}
        for _ in range(random.randint(0, maxedges)):
            neighbour = random.randint(0, maxedges)
            if neighbour not in neighbours:
                graph[node].append(neighbour)
                neighbours.add(neighbour)
    
    return graph

print(genrate(6,2)) 

