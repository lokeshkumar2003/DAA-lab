INF = 9999
nV = 4
def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))

    for r in range(nV):               
        for p in range(nV):           
            for q in range(nV):       
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
        print("Step ",r+1)
        printans(dist)


def printans(dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")
    print("\n")

G = [[0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]]

floyd(G)


#Time complexity O(V^3)