# Task: Shortest Delivery Route


You are given a **city map** represented as a weighted, directed graph.  
Each node represents a **location** (e.g., restaurant, house, store) and each edge represents a **road** between two locations, with a **travel time** as its weight.

You are a delivery driver starting at a given location and must find the **shortest delivery route** (i.e., the minimum total travel time) from your starting location to a customer's house.

Your task is to implement **Dijkstra’s Algorithm** to calculate the shortest path.

---

## Input

- A list of edges representing the city roads. Each edge is a tuple: `(start_location, end_location, travel_time)`.
- A starting location (string or integer).
- A destination location (string or integer).

Example:

```python
edges = [
    ('A', 'B', 5),
    ('A', 'C', 10),
    ('B', 'C', 3),
    ('B', 'D', 9),
    ('C', 'D', 1)
]

start = 'A'
destination = 'D' 
```

---

## Output

- The minimum total travel time from the start to the destination
- The shortest path (list of locations in order)