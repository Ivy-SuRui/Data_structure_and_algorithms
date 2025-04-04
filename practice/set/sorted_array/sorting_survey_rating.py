ratings = [5, 3, 4, 2, 5, 1, 2, 3, 4, 1, 5, 3]

largest_number = max(ratings)

# create a count_array
count_array = [0] * (largest_number +1)

# count each number in the list
for i in ratings:
    count_array[i] += 1

# sorted based on the count array
sorted_rating = []
for i in range(len(count_array)):
    sorted_rating.extend([i]* count_array[i])

print(sorted_rating)

