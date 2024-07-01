import sys

V = 3
INF = sys.maxsize
def minimumCostSimplePath(u, destination, 
						visited, graph):

	if (u == destination):
		return 0

	visited[u] = 1

	ans = INF

	for i in range(V):
		if (graph[u][i] != INF and not visited[i]):
			curr = minimumCostSimplePath(i, destination, 
										visited, graph)
			if (curr < INF):
				ans = min(ans, graph[u][i] + curr)
	visited[u] = 0
	return ans
	

graph = [[INF for j in range(V)]
			for i in range(V)]

visited = [0 for i in range(V)]

graph[0][1] = 1
graph[1][2] = 2
# graph[1][2] = -2
# graph[2][3] = 1
# graph[3][2] = -1
graph[2][0] = 3

s = 0
t = 2

visited[s] = 1

print(minimumCostSimplePath(s, t, visited, graph))

