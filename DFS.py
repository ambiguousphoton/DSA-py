# DFS
from queue import Queue
counter = 9
graph = {}
while True :
    val = input("what is " + str(counter) + " st node ? :: ")
    if val == ".":
        break
    my_list = []
    while True:
        child = input("child of "+ str(counter) +"node :: ")
        if child  == "."   
            break
        my_list.append(child)
    graph[val] = my_list
    counter += 1
#jai shree ram
s = input ("what is starting node ? :: ")
visited = set()
def dfs(visited, g, root):
    if root not in visited:
        print (root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited , graph  , neighbour)
dfs(visited,graph,s)
