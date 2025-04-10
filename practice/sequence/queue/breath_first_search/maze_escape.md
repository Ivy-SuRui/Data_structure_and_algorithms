# Task:

## Problem Description

You are trapped in a 2D maze and need to find the shortest way out.

The maze is represented by a 2D grid of size `N x M`, where:
- `'S'` represents your starting point.
- `'E'` represents the exit.
- `'.'` represents an open path you can walk on.
- `'#'` represents a wall you cannot pass through.

You can move in **four directions**: up, down, left, and right. Diagonal moves are not allowed.

Your task is to determine the **minimum number of steps** required to reach the exit from the start. If no such path exists, return `-1`.

---

## Input Format

You will be given:
- Two integers `N` and `M` (1 ≤ N, M ≤ 1000)
- Followed by `N` lines each containing `M` characters (the maze grid)

---

## Output Format

- A single integer: the minimum number of steps from `'S'` to `'E'`, or `-1` if unreachable.

---

## Example Input

```
5 7
#######
#S....#
#.###.#
#...#.#
###E###
```

## Example Output

```
7
```

---

## Additional Requirements

- Your code should handle mazes as large as 1000x1000 efficiently.
- Avoid using recursion that may cause stack overflow on large inputs.
- Print the actual path (coordinates from S to E) if reachable.
- Measure and print the time it took to find the solution.

---

## Challenge Extension (Optional)

- What if some paths have weights, e.g., `'.'` = 1, `'~'` = 3 (swamp)? Modify your approach accordingly.



BFS logic:

	1.	Initialize a visited set or array
        •	Keeps track of nodes you’ve already explored to avoid revisiting.
        •	In grid problems, this is often a 2D array.
        •	In graph problems, it’s usually a set.
	2.	(Optional) Initialize a parent map or array
        •	Records the node you came from when you reached a new node.
        •	Useful for reconstructing the shortest path later.
	3.	Create a queue (FIFO)
        •	BFS uses a queue to explore nodes level by level.
        •	Start by adding the initial node (e.g., the starting position in a maze).
	4.	Mark the starting node as visited
        •	This prevents it from being processed again.
	5.	While the queue is not empty:
        •	Dequeue the current node.
        •	If the current node is the target (goal, end, match), you can:
        •	Return immediately (for early exit).
        •	Optionally reconstruct the path using the parent array.
	6.	For each neighbor (or adjacent node) of the current node:
        •	Check if the neighbor is within bounds / not blocked (for grids), or exists (for graphs).
        •	If the neighbor has not been visited:
        •	Mark it as visited.
        •	Record its parent if needed.
        •	Enqueue it for future exploration.
	7.	If the queue empties and the target was never found:
        •	There is no path to the goal.
        •	Return failure or an appropriate value (e.g. -1, None, empty list, etc.)
