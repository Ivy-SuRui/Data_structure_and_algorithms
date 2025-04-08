## Task 2: Real-Time Stock Price Tracker *(Best suited for AVL Tree)*

### Scenario  
You’re building a backend for a stock trading app that tracks live stock prices. Each stock has a **ticker symbol** and a **price** that updates frequently.

### Features Required:
- Insert a new stock
- Update a stock’s price
- Remove a stock
- Get the **top 10 highest-priced stocks**
- Get the **rank of a specific stock by price**

### Constraints:
- Thousands of stock entries
- Frequent insertions, updates, deletions
- Queries must be fast and predictable — users expect **realtime response**

### Why AVL fits:
- AVL Tree maintains **strict balance**, so performance is **consistently O(log n)**
- Allows **fast access to ranked elements** (can augment node with subtree size)
- Sorted order (by price) is always maintained
- Can efficiently support **top-N** queries and **rank lookups**
- Much better than plain BST when data is **dynamic and performance-sensitive**