
class Hushtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hush_function(self,key):
        return key % self.size
    
    def insert(self,key,name,GPA):
        index = self.hush_function(key)
        bucket = self.table[index]
        for i, (existing_key, _, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i]=(key,name,GPA)
                return
        bucket.append((key,name,GPA))

    def search(self,key):
        index = self.hush_function(key)
        bucket = self.table[index]
        for exisiting_key, name, GPA in bucket:
            if exisiting_key == key:
                return (name, GPA)
        return None

    def delete(self,key):
        index = self.hush_function(key)
        bucket = self.table[index]
        for i, (existing_key, _, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}:", end=" ")
            for key, name, GPA in bucket:
                print(f"Key: {key}, Name:{name}, GPA: {GPA}")

def main():
    hashtable = Hushtable(10)
    hashtable.insert(101, "Alice", 3.5) 
    hashtable.insert(102, "Bob", 3.8) 
    hashtable.insert(103, "Charlie", 2.9) 
    hashtable.insert(104, "Diana", 3.2) 
    hashtable.insert(105, "Eve", 3.9) 
    hashtable.insert(106, "Frank", 2.8) 
    hashtable.insert(107, "Grace", 3.0) 
    hashtable.insert(108, "Heidi", 3.4)
    hashtable.display()
    hashtable.search(104)
    hashtable.delete(102)
    hashtable.display()

if __name__ == "__main__":
    main()