class Graph:
    def __init__(self,n):
        self.N = n
        self.G = [[0]*n]*n
    def primsMST(self):
        selected_node = [0, 0, 0, 0, 0, 0, 0]
        No_of_edges = 0
        selected_node[0] = True
        Total_cost = 0
        print("Edge - Weight\n")
        while (No_of_edges < N - 1):

            minimum = INF
            a = 0
            b = 0
            for m in range(N):
                if selected_node[m]:
                    for n in range(N):
                        if ((not selected_node[n]) and self.G[m][n]):  
                            # not in selected and there is an edge
                            if minimum > self.G[m][n]:
                                minimum = self.G[m][n]
                                a = m
                                b = n
            Total_cost += self.G[a][b]
            print(str(a) + "-" + str(b) + "   -  " + str(self.G[a][b]))
            selected_node[b] = True
            No_of_edges += 1
        print("\nTotal Cost is: "+str(Total_cost))
  




G = Graph(7) 

G.G = [[0,28,0,0,0,10,0],
         [28,0,16,0,0,0,14],
         [0,16,0,12,0,0,0],
         [0,0,12,0,22,0,18],
         [0,0,0,22,0,25,24],
         [10,0,0,0,25,0,0],
         [0,14,0,18,24,0,0]
        ]

G.primsMST()