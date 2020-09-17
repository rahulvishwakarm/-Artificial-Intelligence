 
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E','F'],
    'C' : ['G'],
    'D' : [],
    'E' : ['F','G'],
    'F' : [],
    'G' : []
}
 
visited = set() 
 
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
 
 
dfs(visited, graph, 'A')
