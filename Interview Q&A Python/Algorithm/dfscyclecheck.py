
def is_tree(N, edges):
    if N != len(edges) + 1:
        return "The Graph is not a tree"
    graph = {}
    visited = set()
    
    #build the graph
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    #Perform DFS to check for cycles
    def dfs(node,parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return "The graph is not a tree"
            if dfs(neighbor, node) == "The graph is not a tree":
                return "The graph is not a tree"
        return "The graph is a tree"
    #check is there are cycles and all nodes are reachable
    return dfs(1, -1)
#Provided input
N = 3
edges = [(1,2),(2,3)]

#check is the graph is a tree and print the output
print(is_tree(N,edges))