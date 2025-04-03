# Practice Task: Fixed-Size LED Strip Controller

## Goal

Simulate controlling a strip of **10 RGB LEDs** using a **static array** (fixed-size list).  
Each LED can be in one of the following states:

- `"."` — LED is off
- `"R"` — Red
- `"G"` — Green
- `"B"` — Blue

You will build a class that models the LED strip using a fixed-size list, and write methods to control it.

---

## Requirements

### 1. Class Name

- The class should be named: `LEDStrip`

---

### 2. Initialization

- The constructor (`__init__`) should create a list of exactly 10 `"."` characters to represent the LED strip.
- This list simulates a static array (fixed size, cannot grow or shrink).

---

### 3. Method: `set(index, color)`

- Description: Turn **on** the LED at the given index with the given color.
- Parameters:
  - `index`: An integer from 0 to 9.
  - `color`: A string that must be `"R"`, `"G"`, or `"B"`.
- Behavior:
  - If `index` is out of range (not between 0–9), print: `"Invalid index."`
  - If `color` is not `"R"`, `"G"`, or `"B"`, print: `"Invalid color."`
  - Otherwise, set the LED at `index` to the given color.

---

### 4. Method: `off(index)`

- Description: Turn **off** the LED at the given index by setting it to `"."`.
- Parameters:
  - `index`: An integer from 0 to 9.
- Behavior:
  - If `index` is out of range, print: `"Invalid index."`
  - Otherwise, set the LED at `index` to `"."`.

---

### 5. Method: `display()`

- Description: Print the current state of the LED strip as a single string (without spaces).
- Example Output: