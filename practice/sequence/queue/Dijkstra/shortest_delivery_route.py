import heapq

def dijkstra(edges, start, destination):
    # Build the graph
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))
    
    # Priority queue: (distance, node, path)
    heap = [(0, start, [start])]
    visited = set()
    
    while heap:
        dist, node, path = heapq.heappop(heap)
        
        if node == destination:
            return dist, path
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (dist + weight, neighbor, path + [neighbor]))
    
    return float('inf'), []

# Example usage
edges = [
    ('A', 'B', 5),
    ('A', 'C', 10),
    ('B', 'C', 3),
    ('B', 'D', 9),
    ('C', 'D', 1)
]

start = 'A'
destination = 'D'

travel_time, path = dijkstra(edges, start, destination)
if travel_time == float('inf'):
    print("Destination unreachable.")
else:
    print(f"Travel Time: {travel_time}")
    print(f"Path: {path}")