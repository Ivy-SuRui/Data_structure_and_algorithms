# You receive two sorted lists of daily sales totals from two different branches.
# You need to merge them into one sorted list for the week’s report.

branch_A = [1200, 1350, 1400, 1550]
branch_B = [1250, 1500, 1300, 1600]

# Goal: Merge the two lists into a single sorted list


Right answer:

use the merge sort:

1. divid the branch into half and recursively sort until you get arrays of size 1
2. merge by compare one item in each list, put it into the list and move to the next item of the list until all elements in that list included
3. put remaining of the other list into the final list