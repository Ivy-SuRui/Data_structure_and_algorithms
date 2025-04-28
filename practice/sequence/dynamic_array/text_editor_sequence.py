class Editor:
    def __init__(self):
        self.buffer = []
        self.cursor = 0

    # insert function
    def insert(self, character):
        self.buffer.insert(self.cursor, character)
        self.cursor += 1


    # delete function
    def delete(self):
        if self.cursor > 0:
            self.buffer.pop(self.cursor-1)
            self.cursor -= 1


    # move the cursor to the left function
    def move_left(self):
        if self.cursor >0:
            self.cursor -= 1


    # move the cursor to the right function
    def move_right(self):
        if self.cursor < len(self.buffer):
            self.cursor += 1

    # display current cursor with _ function
    def display(self):
        final = self.buffer[:]  # make a copy of self.buffer
        final.insert(self.cursor, "_")
        print("".join(final))

def main():
    editor = Editor()
    editor.insert("a")
    editor.insert("b")
    editor.insert("c")
    editor.move_left()
    editor.delete()
    editor.insert("x")
    editor.display()

if __name__ == "__main__":
    main()