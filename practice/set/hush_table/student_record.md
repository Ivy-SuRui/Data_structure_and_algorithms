# Hash Table Practice Task: Student Record System

## Objective
1. Build a hash table from scratch in Python (without using built-in dict).  
Each student record includes:
- `student_id` (int): unique key
- `name` (str)
- `GPA` (float)

---
2. Add functions such as insert, search, delete, display

3. Test:

ht = HashTable(10)

# Insert students
ht.insert(101, "Alice", 3.5)
ht.insert(102, "Bob", 3.8)
ht.insert(103, "Charlie", 2.9)
ht.insert(104, "Diana", 3.2)
ht.insert(105, "Eve", 3.9)
ht.insert(106, "Frank", 2.8)
ht.insert(107, "Grace", 3.0)
ht.insert(108, "Heidi", 3.4)

# Display all
ht.display()

# Search for a student
print("\nSearch 104:", ht.search(104))

# Delete a student
print("\nDeleting 102...")
ht.delete(102)
ht.display()


### Right answer:

use hash table:

1. build a hush table, with dynamic array inside each bucket
2. insert/search/delete function all have to check the key with existing key before doing the function
