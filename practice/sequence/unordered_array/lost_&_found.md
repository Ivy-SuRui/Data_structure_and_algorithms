# Lost & Found Tracker — Data Structure Practice

## Task Description

You are building a **Lost & Found tracking system** for a small train station office. The staff needs a simple way to:

1. **Add a new item** when someone turns it in.
2. **Search for an item** when someone comes to ask about it.
3. **Remove an item** when it is claimed.

There’s **no need to keep the items in any order** — they are just stored in a box. The system should be able to handle around **100 items** max.

---

## Requirements

### Class: `LostAndFound`

#### Properties:
- `items`: internal array to store the items (initially fixed-size, e.g., 100)
- `capacity`: maximum number of items allowed
- `size`: current number of items

---

### Methods:

#### `add_item(item: str) -> None`
- Adds the item to the collection.
- If full, print a message: `"Storage is full!"`

#### `find_item(item: str) -> int`
- Returns the index of the item if found, else returns `-1`.

#### `claim_item(item: str) -> None`
- Removes the item if found.
- Use the **swap-with-last** trick to remove in constant time.
- If not found, print: `"Item not found."`

#### `show_items() -> None`
- Prints the list of items currently in storage.

---

## Example Usage

```python
lf = LostAndFound()
lf.add_item("Red Umbrella")
lf.add_item("Blue Backpack")
lf.show_items()             # Output: ['Red Umbrella', 'Blue Backpack']

lf.claim_item("Red Umbrella")
lf.show_items()             # Output: ['Blue Backpack']

print(lf.find_item("Blue Backpack"))  # Output: 0