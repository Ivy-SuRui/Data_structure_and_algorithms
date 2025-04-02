### Sequence (Abstract data type) Interface (L02, L07)

| Data Structure  | get_at(i) | set_at(i, x) | insert_first(x) | insert_last(x) | insert_at(i, x) | delete_first() | delete_last() | delete_at(i) | Real-Life Example                         | Why Use It                                                                                   |
|-----------------|-----------|---------------|------------------|----------------|------------------|----------------|----------------|----------------|-------------------------------------------|----------------------------------------------------------------------------------------------|
| **Array**       | 1         | 1             | n                | n              | n                | n              | n              | n              | Game board (e.g., chess, sudoku)          | Use when the **size is fixed** and **fast access** is needed; memory layout is predictable.  |
| **Linked List** | n         | n             | 1                | n              | n                | 1              | n              | n              | Undo/Redo buffer, browser history         | Use when **frequent insert/delete at front or middle**; don’t need fast indexing.            |
| **Dynamic Array**| 1        | 1             | n                | 1 (amortized)  | n                | n              | 1 (amortized)  | n              | Search history, dynamic lists in apps     | Use when **list size changes often**; fast average-case appends, auto-resizing saves effort. |


| **Data Structure**        | `build(A)`     | `find(k)`   | `insert(x)`    | `delete(k)`    | `find_min()` | `find_max()` | `find_prev(k)` | `find_next(k)` | **Use Case Example**                         | **Why Use It**                                                                 |
|---------------------------|----------------|-------------|----------------|----------------|--------------|--------------|----------------|----------------|----------------------------------------------|----------------------------------------------------------------------------------|
| **Unordered Array**       | O(n)           | O(n)        | O(n)           | O(n)           | O(n)         | O(n)         | O(n)           | O(n)           | Small collection with simple membership checks | Easy to implement, but slow for large data or frequent updates                   |
| **Sorted Array**          | O(n log n)     | O(log n)    | O(n)           | O(n)           | O(1)         | O(1)         | O(log n)       | O(log n)       | Leaderboards, high scores, sorted leader views | Efficient **search** and **ordering**, but slow **inserts/deletes**             |
| **Direct Access Array**   | O(u)           | O(1)        | O(1)           | O(1)           | O(u)         | O(u)         | O(u)           | O(u)           | Index-based access, bitmaps, counting sort     | Lightning-fast lookups when universe `u` is small and known                     |
| **Hash Table**            | O(n) (expected)| O(1)*       | O(1)*          | O(1)*          | O(n)         | O(n)         | O(n)           | O(n)           | Caches, dictionaries, membership tracking      | Fast average-case performance; poor ordering support; depends on good hashing    |

\* Expected average-case time; may degrade to O(n) in worst-case scenarios (e.g., hash collisions).  
**Note:** `u` = size of the **key universe** (i.e., the total range of possible keys — like 0 to 10⁶). Large `u` = higher memory cost.



### Comparison of Classic Sorting Algorithms

| **Algorithm**     | **Category**              | **Best Case** | **Average Case** | **Worst Case** | **Space** | **Stable?** | **In-Place?** | **Best Use Case**                                                      |
|-------------------|---------------------------|----------------|------------------|----------------|-----------|-------------|----------------|--------------------------------------------------------------------------|
| **Bubble Sort**   | Simple / Quadratic        | O(n)           | O(n²)            | O(n²)          | O(1)      | Yes         | Yes            | When the list is **almost sorted**, or for educational use              |
| **Selection Sort**| Simple / Quadratic        | O(n²)          | O(n²)            | O(n²)          | O(1)      | No          | Yes            | When memory is tight and implementation simplicity matters              |
| **Insertion Sort**| Simple / Quadratic        | O(n)           | O(n²)            | O(n²)          | O(1)      | Yes         | Yes            | Great for **small or nearly sorted** datasets                          |
| **Merge Sort**    | Divide & Conquer          | O(n log n)     | O(n log n)       | O(n log n)     | O(n)      | Yes         | No             | **Large datasets**, stable sorting, or linked lists                     |
| **Quick Sort**    | Divide & Conquer          | O(n log n)     | O(n log n)       | O(n²)          | O(log n)  | No          | Yes            | **General-purpose fast sort**, when average speed is more important     |
| **Heap Sort**     | Heap-based                | O(n log n)     | O(n log n)       | O(n log n)     | O(1)      | No          | Yes            | Good worst-case time, **no extra space needed**                         |
| **Counting Sort** | Counting-based            | O(n + k)       | O(n + k)         | O(n + k)       | O(k)      | Yes         | No             | When sorting **integers in a small range**, super fast                  |
| **Radix Sort**    | Counting-based            | O(nk)          | O(nk)            | O(nk)          | O(n + k)  | Yes         | No             | **Non-comparison sort** for integers, strings, IDs, etc.                |
| **Bucket Sort**   | Counting-based            | O(n + k)       | O(n + k)         | O(n²)          | O(n + k)  | Yes         | No             | Good for **uniformly distributed floating-point numbers**               |
| **TimSort**       | Hybrid (Merge + Insertion)| O(n)           | O(n log n)       | O(n log n)     | O(n)      | Yes         | No             | **Python’s built-in sort**, great for real-world data                   |