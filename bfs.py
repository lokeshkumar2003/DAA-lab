graph = {
  '5' : ['3','7'],
  '3' : ['2', '4','5'],
  '7' : ['5','8'],
  '2' : ['4'],
  '4' : ['3','8'],
  '8' : ['4','7']
}

visited = [] 
queue = []     

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print("Breadth-First Search")
bfs(visited, graph, '7')    # function calling