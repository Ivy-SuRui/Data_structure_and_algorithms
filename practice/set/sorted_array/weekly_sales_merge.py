branch_A = [1200, 1350, 1400, 1550]
branch_B = [1250, 1500, 1300, 1600]

def merge_sort(branch):
    if len(branch) <= 1:
        return branch

    mid = len(branch) // 2
    left = merge_sort(branch[:mid])
    right = merge_sort(branch[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
    
branch_big = branch_A + branch_B  
print(merge_sort(branch_big))

        