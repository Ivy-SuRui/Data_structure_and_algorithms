# Task 1: Build a Mini Text Editor Engine

## Goal:
Create a console-based text editor engine that supports **basic text editing features** — like inserting, deleting, moving the cursor, and undoing actions — by applying what you've learned about **sequences and data structures**.

---

## Features to Implement

### 1. Text Buffer
- Store the current text as a sequence of characters.
- You choose the structure: Python list, linked list, or another.

### 2. Insert Character
- Add a character at the **current cursor position**.

### 3. Delete Character
- Delete a character **before** or **at** the cursor.

### 4. Move Cursor
- Move cursor left or right.
- Prevent moving beyond the start or end of the buffer.


### 5. Display Current State
- Print the text buffer as a string.
- Indicate the cursor position (e.g., with `|` or `_`).

---

## Example Interaction

```python
> insert a
> insert b
> insert c
> move left
> delete
> insert x
> display
# Output: "ax|c"