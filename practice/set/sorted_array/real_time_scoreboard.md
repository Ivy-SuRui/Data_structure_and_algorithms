# You're running a live game scoreboard.
# As each player scores, their score is added to the list.
# You need to insert each new score in the correct position to keep the list sorted in real time.

scores = [10, 15, 12, 8, 20]

# Goal: Maintain a sorted list of scores as each number is added

Right answer:

use the insertion sort:

1. choose the second item
2. compare to the previous item
3. shift the sorted item to the right position, and insert the new item
4. move to the next item and repeat from step 2