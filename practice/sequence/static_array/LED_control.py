class LED_strip:
    def __init__(self):
        self.strip = ["."] * 10

    # set function - turn on the LED with thte given color
    def set(self,index:int,color):
        if 0 <= index < len(self.strip):
            if color in ["R", "G", "B"]:
                self.strip[index] = color
            else:
                print("Doesn't support this colour.")
        else:
            print("Invalid index.")
    # off function -turn off the LED
    def off(self,index):
        if 0 <= index < len(self.strip):
            self.strip[index] = "."
        else:
            print("Invalid index.")
    # display function
    def display(self):
        print("".join(self.strip))
    # clear function
    def clear(self):
        self.strip = "." * 10
    
def main():
    led = LED_strip()
    led.set(1, "R")
    led.set(3, "G")
    led.set(6, "B")
    led.display()
    led.off(6)
    led.display()
    led.clear()
    led.display()

if __name__ == "__main__":
    main()


