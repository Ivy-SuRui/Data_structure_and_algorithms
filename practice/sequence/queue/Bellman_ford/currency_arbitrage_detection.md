# Task 2: Currency Arbitrage Detection (Negative Weight Cycles)

## Problem Description

You are given a list of currency exchange rates, modeled as a directed graph. Each node is a currency, and each edge represents a possible exchange with a given cost (can be negative due to fees or profit margins).

Your task is to determine whether there exists an **arbitrage opportunity** — a cycle in the graph that allows starting with some currency and returning to it with **net gain** (negative cycle).

---

## Input Format

- Two integers `N` and `M` — the number of currencies (nodes) and exchange options (edges) (1 ≤ N ≤ 1000, 0 ≤ M ≤ 10^4)
- `M` lines follow: each line has three values: `u v w`, meaning you can exchange currency `u` to `v` with cost `w` (float or integer, possibly negative)

---

## Output Format

- Output `"YES"` if there's a negative weight cycle (arbitrage possible), otherwise `"NO"`

---

## Example Input

```
4 5
0 1 1
1 2 1
2 3 -3
3 1 1
0 2 10
```

## Example Output

```
YES
```

(Explanation: 1 → 2 → 3 → 1 forms a cycle with total cost = -1)

---

## Notes

- Negative cycles indicate arbitrage opportunities.
- Your algorithm should work even if the graph is not connected.
- Consider using an algorithm that handles negative weights safely.



Logic:

1. relax all edges (v-1) times to find the shortest path if there are no negative cycles

2. relax again, if any edge can still be relaxed, it means there is a negative weight cycle