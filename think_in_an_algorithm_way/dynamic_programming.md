# Dynamic Programming

Dynamic Programming is a method to solve problems by:
- Breaking them into **subproblems**
- Solving each **subproblem once**
- Combining them to form the **overall solution**

---

## DP Framework: **SRTBOT**

Use this 6-step structure to solve any DP problem:

| Step | Meaning                | Description |
|------|------------------------|-------------|
| S    | Subproblem             | What does `dp[i]` or `dp[i][j]` mean? |
| R    | Recurrence Relation    | How to build current `dp[i]` from previous results |
| T    | Topological Order      | The order to compute the subproblems |
| B    | Base Case              | What are the initial values? |
| O    | Original Problem       | Where is the final answer in `dp`? |
| T    | Time Analysis          | What's the time complexity? |

---

## Understanding Prefix / Suffix / Substring

| Term        | Meaning                            | When to Use                          |
|-------------|-------------------------------------|--------------------------------------|
| Prefix      | Beginning portion of string/array   | When building left-to-right          |
| Suffix      | Ending portion                      | When working backwards               |
| Substring   | Continuous chunk                    | When solving problems on segments    |
| Subsequence | Non-continuous subset               | For matching or ordering problems    |

---

## Why Use `max()` or `min()`?

- Use `max()` when the problem wants the **largest/longest/best** solution.
- Use `min()` when it wants the **smallest/cheapest/fewest**.
- Use `+1`, `+cost`, etc. when counting or accumulating.

---

## DP Patterns



### 1. Fibonacci (Simple DP)

**Problem**: Return the nth Fibonacci number.

#### SRTBOT
- **S**: `dp[i] = i-th Fibonacci number`
- **R**: `dp[i] = dp[i-1] + dp[i-2]`
- **T**: `i = 2 → n`
- **B**: `dp[0] = 0`, `dp[1] = 1`
- **O**: `dp[n]`
- **T**: O(n)

#### Structural Pattern
- **Prefix**: We compute the answer using previous values from the beginning up to `i`.
- **Function Used**: `+` (no `max()` or `min()`)  
  **Reason**: It's just accumulation, not optimization.

```python
def fib(n):
    if n <= 1: return n
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

---

### 2. Coin Change (Minimum Coins)

**Problem**: Given coin denominations and a target amount, return the minimum number of coins to make the amount. Return -1 if impossible.

#### SRTBOT
- **S**: `dp[i] = min number of coins to make amount i`
- **R**: `dp[i] = min(dp[i - coin] + 1)` for all valid coins
- **T**: `i = 1 → amount`
- **B**: `dp[0] = 0`
- **O**: `dp[amount] if finite else -1`
- **T**: O(amount × len(coins))

#### Structural Pattern
- **Prefix**: We're building answers from smaller amounts to larger ones.
- **Function Used**: `min()`  
  **Reason**: We're minimizing the number of coins needed to reach a certain amount.

```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

### 3. Longest Increasing Subsequence (LIS)

**Problem**: Given an array of integers, return the length of the longest strictly increasing subsequence.

#### SRTBOT
- **S**: `dp[i] = length of LIS ending at index i`
- **R**: `dp[i] = max(dp[j] + 1)` for all `j < i` and `nums[j] < nums[i]`
- **T**: `i = 0 → n-1`, inner `j < i`
- **B**: `dp[i] = 1`
- **O**: `max(dp)`
- **T**: O(n²)

#### Structural Pattern
- **Prefix + Subsequence**: We build from earlier indexes and consider non-contiguous sequences.
- **Function Used**: `max()`  
  **Reason**: We want the longest increasing subsequence possible.

```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

---

### 4. Longest Common Subsequence (LCS)

**Problem**: Return the length of the longest subsequence common to both strings.

#### SRTBOT
- **S**: `dp[i][j] = LCS length of s1[:i] and s2[:j]`
- **R**: if `s1[i-1] == s2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`, else: `max(dp[i-1][j], dp[i][j-1])`
- **T**: `i = 1 → n`, `j = 1 → m`
- **B**: `dp[0][*] = dp[*][0] = 0`
- **O**: `dp[n][m]`
- **T**: O(n × m)

#### Structural Pattern
- **Prefix + Subsequence**: We compare prefixes of the strings while allowing gaps.
- **Function Used**: `max()`  
  **Reason**: We want the longest matching sequence between the two.

```python
def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
```

---

### 5. Rod Cutting (Unbounded Knapsack)

**Problem**: Cut a rod of length `n` to maximize value. You can use pieces of any length multiple times.

#### SRTBOT
- **S**: `dp[i] = max value for rod length i`
- **R**: `dp[i] = max(dp[i], price[j - 1] + dp[i - j])`
- **T**: Outer `i = 1 → n`, inner `j = 1 → i`
- **B**: `dp[0] = 0`
- **O**: `dp[n]`
- **T**: O(n²)

#### Structural Pattern
- **Prefix**: We grow the rod from 0 to n.
- **Function Used**: `max()`  
  **Reason**: We want the highest possible total value.

```python
def rod_cutting(prices, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j])
    return dp[n]
```

---

### 6. Subset Sum

**Problem**: Determine if any subset of numbers adds up to a target sum.

#### SRTBOT
- **S**: `dp[i] = True if sum i is possible`
- **R**: `dp[i] = dp[i] or dp[i - num]` for all nums
- **T**: For each num, loop `i = target → num`
- **B**: `dp[0] = True`
- **O**: `dp[target]`
- **T**: O(n × target)

#### Structural Pattern
- **Prefix**: Build possible sums as we go.
- **Function Used**: `or`  
  **Reason**: We want to check if there's **any** valid subset.

```python
def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]
```

---

### 7. DAG Max Path

**Problem**: In a DAG, find the length of the longest path from any node.

#### SRTBOT
- **S**: `dp[u] = longest path starting at u`
- **R**: `dp[v] = max(dp[v], dp[u] + weight)`
- **T**: Topological order
- **B**: `dp[u] = 0` for all nodes
- **O**: `max(dp)`
- **T**: O(V + E)

#### Structural Pattern
- **Prefix-like on DAG**: Process in topological order.
- **Function Used**: `max()`  
  **Reason**: We want the longest possible path.

```python
from collections import defaultdict, deque

def dag_longest_path(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    dp = [0] * n
    queue = deque(i for i in range(n) if indegree[i] == 0)
    topo = []

    while queue:
        u = queue.popleft()
        topo.append(u)
        for v, _ in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    for u in topo:
        for v, w in graph[u]:
            dp[v] = max(dp[v], dp[u] + w)

    return max(dp)
```

---

### 8. APSP (Floyd-Warshall)

**Problem**: Find shortest distances between every pair of nodes.

#### SRTBOT
- **S**: `dp[i][j] = shortest distance from i to j`
- **R**: `dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])`
- **T**: Triple loop `k, i, j`
- **B**: `dp[i][j] = edge weight` or inf
- **O**: `dp[i][j]`
- **T**: O(n³)

#### Structural Pattern
- **Matrix update (not prefix)**: Update in all directions.
- **Function Used**: `min()`  
  **Reason**: We want the shortest possible path.

```python
def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

---

### 9. Arithmetic Parenthesization (Matrix Chain Multiplication)

**Problem**: Given a sequence of matrices, find the most efficient way to multiply them.  
Each matrix `A[i]` has dimension `p[i-1] × p[i]`.  
You must decide where to place parentheses to **minimize the number of scalar multiplications**.

#### SRTBOT
- **S**: `dp[i][j] = minimum cost of multiplying matrices A[i] to A[j]`
- **R**: `dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j])` for all `k` in `[i, j-1]`
- **T**: Solve for chain lengths from 2 to n, then all valid `i`, `j`
- **B**: `dp[i][i] = 0` (single matrix = no multiplication)
- **O**: `dp[1][n-1]`
- **T**: O(n³)

#### Structural Pattern
- **Substring (range DP)**: The problem is solved for ranges `[i, j]` of the array.
- **Function Used**: `min()`  
  **Reason**: We want the minimum cost to compute the matrix product.

```python
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0]*n for _ in range(n)]
    for l in range(2, n+1):  # l = chain length
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]
```

---

### 10. Piano (1,2,3-step staircase variant)

**Problem**: How many ways to play `n` notes if you can press 1, 2, or 3 notes at once.

#### SRTBOT
- **S**: `dp[i] = number of ways to play i notes`
- **R**: `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`
- **T**: `i = 3 → n`
- **B**: `dp[0] = 1`, `dp[1] = 1`, `dp[2] = 2`
- **O**: `dp[n]`
- **T**: O(n)

#### Structural Pattern
- **Prefix**: We're solving for every note from 0 to n.
- **Function Used**: `+` (accumulation)  
  **Reason**: Count all ways to reach a point.

```python
def piano_ways(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]
```

---

### 11. Pseudopolynomial Concept

**Problem**: Applies to subset sum, knapsack, coin change, etc.

#### Key Idea
- Time complexity is `O(n × target)` or `O(n × W)`
- This is fast if target/W is small — **but slow if they're large**

#### Structural Pattern
- **Prefix** (usually)
- **Function Used**: `min()`, `max()`, `or` depending on problem
- **Reason**: Optimization over all subsets/choices

---
