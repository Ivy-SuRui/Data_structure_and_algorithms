# Emergency Room Patient Management System

## Task Overview

You are developing a core component of an emergency room (ER) management system. The ER must manage patients based on how critical their condition is.

Each patient has:
- `name` (string): The patient's name.
- `urgency_level` (integer: 1–100): The higher the number, the more critical the condition.

The system needs to support the following operations efficiently:

### 1. Add a New Patient
- Input: `name`, `urgency_level`
- Behavior: Add the patient to the ER queue.

### 2. See the Most Urgent Patient
- Output: The patient with the highest urgency level (do not remove them).
- Behavior: Return the most urgent patient's info.

### 3. Call the Most Urgent Patient
- Behavior: Remove and return the patient with the highest urgency level.

### 4. Update a Patient's Urgency Level
- Input: `name`, `new_urgency_level`
- Behavior: Update the urgency level of a patient already in the queue.

### 5. (Optional) See Top 10 Most Urgent Patients
- Output: A list of the 10 most urgent patients (do not remove them).

## Requirements
- The system must efficiently handle a high volume of patients.
- If multiple patients have the same urgency level, prioritize the one who arrived first.
- Every operation should maintain patient data integrity.
- No patient should be "lost" from the system due to inefficient data handling.

## Hint
You might need a combination of data structures to:
- Quickly find the most urgent patient
- Handle updates efficiently
- Preserve arrival order when urgency levels match

Design and justify your data structure choice accordingly.



Use bianry heap:

1. need to build a heap array

2. push info into heap, either min_heap or max_heap (python's heapq module turns this list into a min-heap by default)

3. use pop function to give the minmum one or maximum one

4. if you need to use the value again, you need to pop and store it in a temp for further push
