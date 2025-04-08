class Book:
    def __init__(self,title,ISBN,author):
        self.title = title
        self.ISBN = ISBN
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.ISBN})"


class BST:
    def __init__(self,book):
        self.book = book
        self.left = None
        self.right = None

class Library_catelog:
    def __init__(self):
        self.root = None

    # insert a book by title
    def insert(self,node,book):
        if node is None:
            return BST(book)
        if book.title == node.book.title:
            return node.book
        elif book.title < node.book.title:
            node.left = self.insert(node.left, book)
        else:
            node.right = self.insert(node.right, book)
        return node
        
    def add_book(self,title,ISBN,author):
        book = Book(title,ISBN,author)
        self.root = self.insert(self.root, book)

    # search a book by exact title
    def search(self,node,title):
        if node is None:
            return None
        if title == node.book.title:
            return node.book
        elif title < node.book.title:
            return self.search(node.left,title)
        else:
            return self.search(node.right, title)
    def find(self,title):
        book = self.search(self.root, title)
        if book == None:
            print("Not found.")
        else:
            print("Found {title}")
            return book

    # delete a book
    def delete(self,node,title):
        if node is None:
            return node
        if title < node.book.title:
            node.left = self.delete(node.left, title)
        elif title > node.book.title:
            node.right = self.delete(node.right, title)
        else:
            # if node is a leaf
            if node.left is None and node.right is None:
                return None
            # if node has a left child:
            elif node.right:
                pred = self.get_max(node.left)
                node.book, pred.book = pred.book, node.book
                node.left = self.delete(node.left, pred.book.title)
            # if node has a right child:
            elif node.left:
                suc = self.get_min(node.right)
                node.book, suc.book = suc.book, node.book
                node.right = self.delete(node.right,suc.book.title)
        return node
    def remove(self,title):
        self.root = self.delete(self.root, title)
    def get_max(self,node):
        current = node
        while current.right:
            current = current.right
        return current
    def get_min(self,node):
        current = node
        while current.left:
            current = current.left
        return current

    # list all books in alphabetical order by title
    def in_order(self,node,result):
        if node:
            self.in_order(node.left, result)
            result.append(node.book)
            self.in_order(node.right, result)
    def list(self):
        result = []
        self.in_order(self.root, result)
        return result
    
def main():
    catalog = Library_catelog()
    catalog.add_book("C", "978-C", "Author C")
    catalog.add_book("A", "978-A", "Author A")
    catalog.add_book("B", "978-B", "Author B")
    catalog.add_book("E", "978-E", "Author E")
    catalog.add_book("D", "978-D", "Author D")

    print("All books:")
    for book in catalog.list():
        print(book)

    catalog.remove("C")
    print("\nAll books after deletion:")
    for book in catalog.list():
        print(book)

if __name__ == "__main__":
    main()

        