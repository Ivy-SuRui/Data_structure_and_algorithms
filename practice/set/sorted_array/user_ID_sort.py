employee_ids = [482915, 103254, 789123, 456789, 321654, 654321, 219876, 987654]


def counting_sort_by_digit(arr, digit_place):
    count = [[] for _ in range(10)]  # Create 10 buckets for digits 0–9
    for num in arr:
        digit = (num // digit_place) % 10
        count[digit].append(num)  # Place number in appropriate bucket
    
    result = []
    for bucket in count:
        for num in bucket:
            result.append(num)
    return result  

def radix_sort(arr):
    digit_place = 1
    for _ in range(6):
        arr = counting_sort_by_digit(arr, digit_place)
        digit_place *= 10
    return arr

sorted_ids = radix_sort(employee_ids)
print(sorted_ids)
                        

