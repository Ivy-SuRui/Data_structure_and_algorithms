# Each patient arriving at the emergency room is assigned a severity level from 1 to 10.
# You need to sort them so the most severe cases come first.

patients = [
    ("Alice", 4),
    ("Bob", 9),
    ("Charlie", 2),
    ("David", 10),
    ("Eva", 4),
    ("Frank", 7)
]

# Goal: Sort patients by severity (descending)


Right answer:

use selection sort:

1. choose one
2. compare this one to the rest
3. swap the max or min to the right position
4. return the rest to the 1
