## Task 1: Simple Library Catalog System *(Best suited for Binary Search Tree)*

### Scenario  
You’re designing a lightweight book catalog system for a small rural library. Each book is stored with a **title**, **ISBN**, and **author**.

### Features Required:
- Insert a new book (by title)
- Delete a book
- Search a book by exact title
- List all books in alphabetical order by title

### Constraints:
- Total number of books is under 200
- Book additions/deletions are infrequent
- Most books are inserted in random order (not strictly sorted)

### Why BST fits:
- Dataset is **small**, so worst-case performance is tolerable
- Operations are not time-critical
- Simple BST keeps implementation lightweight
- Sorted traversal (by title) is easy with in-order traversal
- You don’t need strict performance guarantees — just **basic sorting and search**


notes:

1. insert nodes

2. delete nodes:

    2.1 if it is a leaf, detch from parent and return

    2.2 if it has children,  if has a left child, swap with the predecessor and recurse; if has a right child, swap with the successor and recurse
