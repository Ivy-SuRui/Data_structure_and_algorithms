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

---

### 1. Fibonacci (Simple DP)

**Problem**: Return the nth Fibonacci number.

#### SRTBOT
- **S**: `dp[i] = i-th Fibonacci number`
- **R**: `dp[i] = dp[i-1] + dp[i-2]`
- **T**: `i = 2 → n`
- **B**: `dp[0] = 0`, `dp[1] = 1`
- **O**: `dp[n]`
- **T**: O(n)

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

**Problem**: Given `coins[]` and a target `amount`, return the **fewest coins** to make that amount.

#### SRTBOT
- **S**: `dp[i] = min coins to make amount i`
- **R**: `dp[i] = min(dp[i - coin] + 1 for coin in coins)`
- **T**: `i = 1 → amount`
- **B**: `dp[0] = 0`
- **O**: `dp[amount]`
- **T**: O(amount × len(coins))

```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

### 3. Longest Increasing Subsequence (LIS)

**Problem**: Find the length of the longest increasing subsequence in an array.

#### SRTBOT
- **S**: `dp[i] = length of LIS ending at index i`
- **R**: `dp[i] = max(dp[j] + 1) for all j < i if nums[j] < nums[i]`
- **T**: `i = 0 → n-1`
- **B**: `dp[i] = 1`
- **O**: `max(dp)`
- **T**: O(n²)

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

**Problem**: Given two strings, return the length of their longest common subsequence.

#### SRTBOT
- **S**: `dp[i][j] = LCS length of s1[:i] and s2[:j]`
- **R**:  
  - If match: `dp[i][j] = dp[i-1][j-1] + 1`
  - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
- **T**: `i = 1 → n`, `j = 1 → m`
- **B**: `dp[0][*] = dp[*][0] = 0`
- **O**: `dp[n][m]`
- **T**: O(n×m)

```python
def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]
```

---

### 5. Longest Path in DAG

**Problem**: Find the longest path in a Directed Acyclic Graph (DAG) from any node.

#### SRTBOT
- **S**: `dp[u] = max path length from u`
- **R**: `dp[v] = max(dp[v], dp[u] + w)`
- **T**: Topological sort
- **B**: `dp[src] = 0` (or all 0s)
- **O**: `max(dp)`
- **T**: O(V + E)

```python
from collections import defaultdict, deque

def dag_longest_path(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    dp = [0] * n
    queue = deque([i for i in range(n) if indegree[i] == 0])
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

## Final Tips

- Visualize the **state definition** (`dp[i]`, `dp[i][j]`)
- Build intuition by identifying **prefix/suffix/substring** patterns
- Write out the SRTBOT steps explicitly before coding
- Start with bottom-up tabulation; optimize later

---