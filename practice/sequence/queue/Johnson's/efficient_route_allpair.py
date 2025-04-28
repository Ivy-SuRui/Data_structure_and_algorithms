import heapq

INF = float('inf')

def johnson(N, edges):
    # Step 1: Add a new node 'N' with edges (N -> v) of weight 0
    new_edges = edges[:]
    for v in range(N):
        new_edges.append((N, v, 0))
    
    # Step 2: Run Bellman-Ford from node N to get h(v)
    h = [INF] * (N + 1)
    h[N] = 0

    for _ in range(N):
        for u, v, w in new_edges:
            if h[u] != INF and h[u] + w < h[v]:
                h[v] = h[u] + w

    # No negative cycles assumed, otherwise Bellman-Ford would detect here

    # Step 3: Reweight edges
    graph = [[] for _ in range(N)]
    for u, v, w in edges:
        # w' = w + h[u] - h[v]
        new_weight = w + h[u] - h[v]
        graph[u].append((v, new_weight))

    # Step 4: For each node, run Dijkstra
    def dijkstra(start):
        dist = [INF] * N
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        return dist

    result = []
    for u in range(N):
        dists = dijkstra(u)
        # Revert reweighting: real_dist(u,v) = dists[v] + h[v] - h[u]
        row = []
        for v in range(N):
            if dists[v] == INF:
                row.append("INF")
            else:
                real_dist = dists[v] + h[v] - h[u]
                row.append(str(real_dist))
        result.append(row)

    return result

# Read input
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Solve
matrix = johnson(N, edges)

# Print output
for row in matrix:
    print(' '.join(row))