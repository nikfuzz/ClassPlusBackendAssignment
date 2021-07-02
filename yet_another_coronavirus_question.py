class Graph:
    def __init__(self, n) -> None:
        inf = float('inf')
        self.graph = [[inf for j in range(n)] for i in range(n)]
        self.v = n

    # function to add edge in our adj matrix
    def addEdge(self, u, v, w=1):
        self.graph[u][v] = w
    
    # using Floyd Warshall as h == n in worst case
    def shortestPath(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if self.graph[i][k] + self.graph[k][j] < self.graph[i][j]:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]

# standard input
n, h, x = map(int, input().split())

# initialize graph
gr = Graph(n)

hotspots = [int(x) for x in input().split()]

# Adding all the n-1 roads with default weight 1
for i in range(n-1):
    u, v = map(int,input().split())
    gr.addEdge(u-1,v-1)
    gr.addEdge(v-1,u-1)

# calculating shortest path from one city to another
gr.shortestPath()

# Final answer array
ans = [i for i in range(1,n+1)]

# For each hotspot we need to check which cities are at an atmost dist of x
# We need to take the intersection of all such cities, i.e, the epicenters must be atmost x dist away from all the hotspots
for i in range(len(hotspots)):
    z = hotspots[i]-1
    vicinity = []
    for y in range(n):
        if gr.graph[z][y] <= x:
            vicinity.append(y+1)
    ans = set(ans) & set(vicinity)

# Final number of cities
print(len(ans))

# Time complexity O(n^3)
# Space Complexity O(n^2)