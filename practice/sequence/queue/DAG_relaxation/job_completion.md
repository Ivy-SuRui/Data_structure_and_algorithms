# Task 1: Fastest Job Completion (Directed Acyclic Graph)

## Problem Description

You are given `N` jobs labeled `0` to `N-1`, and some jobs depend on others. A job can’t start until all its prerequisites are completed. Each job takes a certain amount of time to complete.

Your task is to determine the **earliest possible time** each job can be completed.

---

## Input Format

- An integer `N` — the number of jobs (1 ≤ N ≤ 10^5)
- An array `T[0...N-1]` where `T[i]` is the time it takes to finish job `i`
- An integer `M` — the number of dependencies
- `M` lines follow: each line has two integers `u v`, meaning job `u` must finish **before** job `v` can begin.

---

## Output Format

- Output `N` integers: the earliest time each job can be completed.

---

## Example Input

```
5
3 2 1 4 6
4
0 2
1 2
2 3
3 4
```

## Example Output

```
3 2 4 8 14
```

(Explanation: Job 0 finishes at 3, Job 1 at 2, Job 2 at max(3,2)+1=4, Job 3 at 4+4=8, Job 4 at 8+6=14)

---

## Notes

- The job dependency graph is guaranteed to be a **DAG**.
- Aim for an efficient solution using topological principles.
- Handle large inputs efficiently (up to 10^5 nodes and edges).



DAG relaxation logic:

1. create a graph to store the dependencies (usually an adjacency list)

2. create an array to track how many prerequisties each node has (it helps us know when a node is ready to be processed)

3. create an array to store the earliest (or longest) completion time for each node

4. create a queue and all nodes with no prerequisties 

5. do the relaxation in topological order