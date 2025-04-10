# Practice Task: Island Counter

## Problem Description

You are given a 2D grid map of `'1'`s (land) and `'0'`s (water). An island is formed by connecting **adjacent lands horizontally or vertically**. 

You need to determine the **total number of islands** in the map.

Two `'1'`s are part of the same island if they are directly connected up, down, left, or right — **diagonal connections do not count**.

---

## Input Format

- Two integers `N` and `M` representing the number of rows and columns (1 ≤ N, M ≤ 1000)
- Followed by `N` lines of strings, each of length `M`, consisting only of `'1'`s and `'0'`s.

---

## Output Format

- A single integer: the total number of islands.

---

## Example Input

```
4 5
11000
11000
00100
00011
```

## Example Output

```
3
```

---

## Additional Requirements

- Your solution should efficiently handle large grids up to 1000x1000.
- Once you visit a piece of land (`'1'`), make sure you don't visit it again.
- You may modify the input grid or maintain a separate visited matrix.

---

## Challenge Extension (Optional)

- Modify your code to not only count islands but also return a list of their sizes (i.e., how many land cells each island contains).
- Can you do it using **recursion**? How about without recursion (explicit stack)?


DFS Logic:

1. Initialize a visited set or array
	•	Tracks nodes you’ve already explored to avoid infinite loops or redundant work.
	•	For grid problems: usually a 2D boolean array.
	•	For general graphs: typically a set of visited nodes.

⸻

2. (Optional) Initialize a parent map or array
	•	Stores where you came from to reach each node.
	•	Useful for reconstructing a path, especially in applications like maze solving or tracing back from a target node.

3. Choose a DFS strategy

DFS can be done in two ways:
	•	Recursive: Let the call stack handle the depth.
	•	Iterative: Use your own stack (LIFO) to manage traversal manually.

⸻

4. Mark the starting node as visited
	•	Do this immediately when you process the node to prevent revisiting it during deeper recursive or stack-based exploration.

⸻

5. Visit each neighbor (or adjacent node)
	•	For each direction in a grid (up, down, left, right) or for each connected node in a graph:
	•	Check if the neighbor is within bounds / valid / not blocked.
	•	If the neighbor has not been visited:
        •	Mark it as visited.
	    •	(Optional) Record the parent.
	    •	Recursively call DFS on the neighbor (if using recursion), or
	    •	Push the neighbor onto the stack (if using iterative DFS).

⸻

6. Continue until all reachable nodes are visited
	•	In recursive DFS: the function will naturally finish once all branches are fully explored.
	•	In iterative DFS: keep popping from the stack until it’s empty.

7. (Optional) Post-processing
	•	After DFS finishes, you can:
	•	Count connected components
	•	Reconstruct paths (if parent map is used)
	•	Gather information like max depth, node values, etc.