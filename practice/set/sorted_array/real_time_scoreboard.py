scores = [10, 15, 12, 8, 20]

for i in range(1,len(scores)):
    compared_item = scores[i]
    j = i -1
    while j>=0 and compared_item > scores[j]:
        scores[j+1] = scores[j]
        j -= 1
    scores[j+1] = compared_item

for score in scores:
    print(score)
            
        