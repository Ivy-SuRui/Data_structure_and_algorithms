# Task: Efficient Route Planner for All Pairs (Sparse Graph with Possible Negative Weights)

## Problem Description

You are tasked with writing a navigation tool for a country with complex road networks. Some roads are cost-saving (negative weights), but **no cycles allow infinite savings** (no negative cycles).

You need to compute the **shortest travel cost between every pair of cities**.

---

## Input Format

- Two integers `N` and `M` — the number of cities (nodes) and roads (edges) (1 ≤ N ≤ 1000, 1 ≤ M ≤ 10000)
- Then `M` lines follow: each contains three integers `u v w` — a directed road from `u` to `v` with cost `w` (can be negative)

---

## Output Format

- An `N x N` matrix: each row `i` contains `N` space-separated values: the shortest cost from city `i` to city `j`.
- If a city `j` is unreachable from `i`, print `"INF"` for that entry.

---

## Example Input

```
4 5
0 1 2
0 2 4
1 2 -3
2 3 2
3 1 1
```

## Example Output

```
0 2 -1 1
INF 0 -3 -1
INF 1 0 2
INF 1 -2 0
```

---

## Notes

- There are **no negative weight cycles**.
- You need an efficient algorithm that handles sparse graphs with negative weights.
- Brute-force Floyd-Warshall will be too slow for maximum constraints.