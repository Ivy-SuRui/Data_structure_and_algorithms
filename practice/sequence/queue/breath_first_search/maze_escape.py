from collections import deque
import time

def read_maze():
    N, M = map(int, input().split())
    maze = []
    for _ in range(N):
        maze.append(list(input().strip()))
    return N, M, maze

def find_start_end(maze):
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "E":
                end = (i, j)
    return start, end


def bfs_maze(N,M,maze,start,end):
    visited = [[False] * M for _ in range(N)]
    parent = [[None] * M for _ in range(N)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    # possible direction: left, right, down, up
    directions = {(-1,0),(1,0),(0,-1),(0,1)}
    while queue:
        x, y = queue.popleft()
        if (x,y) == end:
            path = []
            while (x,y) != start:
                path.append((x,y))
                x, y = parent[x][y]
            path.append(start)
            path.reverse()
            return len(path)-1, path
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited [nx][ny] and maze[nx][ny] != "#":
                    visited[nx][ny] = True
                    parent[nx][ny] = (x,y)
                    queue.append((nx,ny))

    return -1, []

def main():
    N, M, maze = read_maze()
    start, end = find_start_end(maze)

    
    t0 = time.time()
    steps, path = bfs_maze(N, M, maze, start, end)
    t1 = time.time()

    print("Minimum steps:", steps)
    if steps != -1:
        print("Path:")
        for coord in path:
            print(coord)
    else:
        print("No path found.")
    print(f"Time taken: {t1 - t0:.6f} seconds")

if __name__ == "__main__":
    main()



