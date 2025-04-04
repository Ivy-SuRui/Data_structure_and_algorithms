patients = [ ("Alice", 4), ("Bob", 9), ("Charlie", 2), ("David", 10), ("Eva", 4), ("Frank", 7) ]

n = len(patients)

for i in range(n):
    most_severe_index = i
    for j in range(i+1, n):
        if patients[j][1] > patients[most_severe_index][1]:
            most_severe_index = j
        patients[i],patients[most_severe_index] = patients[most_severe_index], patients[i] # swap syntax 
for patient in patients:
    print(patient)