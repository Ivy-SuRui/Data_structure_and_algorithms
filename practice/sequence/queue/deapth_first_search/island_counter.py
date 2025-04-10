import sys
sys.setrecursionlimit(1000000)

def read_grid():
    N, M = map(int, input().split())
    grid = (list(input().strip() for _ in range(N)))
    return N, M, grid

def dfs(N,M,x,y,grid,visited):
    stack = [(x,y)]
    visited[x][y] = True
    size = 1
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == "1" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx,ny))
                    size +=1
    return size

def count_island(N,M,grid):
    visited = [[False]*M for _ in range(N)]
    count = 0
    sizes = []

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "1" and not visited[i][j]:
                size = dfs(N,M,i,j,grid,visited)
                count += 1
                sizes.append(size)

    return count, sizes
                           

def main():
    N, M, grid = read_grid()
    count, sizes = count_island(N, M, grid)
    print(f"Number of islands: {count}")
    print(f"Sizes of islands: {sizes}")

if __name__ == "__main__":
    main()


