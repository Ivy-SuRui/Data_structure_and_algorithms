from collections import deque

def fast_completion(N,edges,times):
    graph = [[] for _ in range(N)]
    prerequisites = [0] * N
    earliest_time = [0] * N

    for u, v in edges:
        graph[u].append(v)
        prerequisites[v] += 1

    queue = deque()

    # initial task to start with no prerequisites
    for i in range(N):
        if prerequisites[i] == 0:
            earliest_time[i] = times[i]
            queue.append(i)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            earliest_time[v] = max(earliest_time[v], earliest_time[u]+times[v])
            prerequisites[v] -= 1
            if prerequisites[v] == 0:
                queue.append(v)

    return earliest_time

def main():
    N = 5
    times = [3, 2, 1, 4, 6]
    edges = [(0, 2), (1, 2), (2, 3), (3, 4)]
    result = fast_completion(N, edges,times)
    print("Earliest completion times:", result)

if __name__ == "__main__":
    main()