### Task: Sort a List of 1 million 8-digit integers (e.g., user IDs)

employee_ids = [482915, 103254, 789123, 456789, 321654, 654321, 219876, 987654]

sort this list in ascending order 


Right answer:

use radix sort (LSD):

1. decide sorted from leftmost or rightmost (consider significance)
2. this time, from the rightmost, sorted (counting sort) by 1s digit, 10 digits, ... 100000 digits (loop)
