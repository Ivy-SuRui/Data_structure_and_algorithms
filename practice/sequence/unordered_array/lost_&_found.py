class Lost_found:
    def __init__(self,capacity = 100):
        self.capacity = capacity
        self.item = [None] * capacity
        self.size = 0  
    # add item
    def add_item(self,item_name):
        if self.size >= self.capacity:
            print("Storage is full.")
        else:
            self.item[self.size] = item_name
            self.size += 1
    # find item
    def find_item(self, item_name):
        for i in range(self.size):
            if self.item[i] == item_name:
                print (f"{item_name} found.")
                return i
            else:
                print("No found.")
                return None
    # claim item
    def claim_item(self,item_name):
        index = self.find_item(item_name)
        if index == None:
            return
        self.item[index] = self.item[self.size - 1]
        self.item[self.size] = None
        self.size -= 1
    # show items
    def show_items(self):
        print(self.item[:self.size])

def main():
    lf = Lost_found()
    lf.add_item("Red Umbrella")
    lf.add_item("Blue Backpack")
    lf.show_items()

    lf.claim_item("Red Umbrella")
    lf.show_items() 

    lf.find_item("Red Umbrella")

if __name__ == "__main__":
    main()      