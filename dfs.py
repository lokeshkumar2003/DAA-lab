graph = {
  '5' : ['3','7'],
  '3' : ['2', '4','5'],
  '7' : ['5','8'],
  '2' : ['4'],
  '4' : ['3','8'],
  '8' : ['4','7']
}

visited = set() 

def dfs(visited, graph, node):   
    if node not in visited:
        print (node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Depth-First Search")
dfs(visited, graph, '2')