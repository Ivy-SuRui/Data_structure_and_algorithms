class AVLNode:
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1  # for rank queries


class StockTracker:
    def __init__(self):
        self.root = None
        self.ticker_map = {}  # ticker -> (price, node)

    # --------- Public Methods ---------
    def insert(self, ticker, price):
        if ticker in self.ticker_map:
            self.update(ticker, price)
        else:
            self.root = self._insert(self.root, ticker, price)

    def update(self, ticker, new_price):
        if ticker in self.ticker_map:
            self.root = self._delete(self.root, ticker)
            del self.ticker_map[ticker]
        self.root = self._insert(self.root, ticker, new_price)

    def remove(self, ticker):
        if ticker in self.ticker_map:
            self.root = self._delete(self.root, ticker)
            del self.ticker_map[ticker]

    def get_top_10(self):
        result = []
        self._reverse_inorder(self.root, result, 10)
        return result

    def get_rank(self, ticker):
        if ticker not in self.ticker_map:
            return -1
        node_price = self.ticker_map[ticker][0]
        return self._get_rank(self.root, node_price, ticker)

    # --------- AVL Tree Internal Methods ---------
    def _height(self, node):
        return node.height if node else 0

    def _size(self, node):
        return node.size if node else 0

    def _update_stats(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node.size = 1 + self._size(node.left) + self._size(node.right)

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_stats(y)
        self._update_stats(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_stats(x)
        self._update_stats(y)
        return y

    def _balance(self, node):
        self._update_stats(node)
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _insert(self, node, ticker, price):
        if not node:
            new_node = AVLNode(ticker, price)
            self.ticker_map[ticker] = (price, new_node)
            return new_node
        if (price, ticker) > (node.price, node.ticker):
            node.right = self._insert(node.right, ticker, price)
        else:
            node.left = self._insert(node.left, ticker, price)
        return self._balance(node)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node, ticker):
        if not node:
            return None
        if ticker == node.ticker:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.ticker = temp.ticker
            node.price = temp.price
            self.ticker_map[node.ticker] = (node.price, node)
            node.right = self._delete(node.right, temp.ticker)
        elif (self.ticker_map[ticker][0], ticker) < (node.price, node.ticker):
            node.left = self._delete(node.left, ticker)
        else:
            node.right = self._delete(node.right, ticker)
        return self._balance(node)

    def _reverse_inorder(self, node, result, limit):
        if not node or len(result) >= limit:
            return
        self._reverse_inorder(node.right, result, limit)
        if len(result) < limit:
            result.append((node.ticker, node.price))
            self._reverse_inorder(node.left, result, limit)

    def _get_rank(self, node, price, ticker):
        if not node:
            return 0
        if (price, ticker) < (node.price, node.ticker):
            return self._get_rank(node.left, price, ticker)
        elif (price, ticker) > (node.price, node.ticker):
            return self._size(node.left) + 1 + self._get_rank(node.right, price, ticker)
        else:
            return self._size(node.right) + 1  # 1-based rank (highest = 1)

# -------------------
# Example Main Program
# -------------------

def main():
    tracker = StockTracker()

    tracker.insert("AAPL", 150)
    tracker.insert("GOOGL", 2800)
    tracker.insert("AMZN", 3400)
    tracker.insert("TSLA", 700)
    tracker.insert("MSFT", 299)
    tracker.insert("NFLX", 590)
    tracker.insert("META", 330)
    tracker.insert("NVDA", 750)
    tracker.insert("BABA", 210)
    tracker.insert("ORCL", 90)
    tracker.insert("IBM", 145)

    print("Top 10 stocks:")
    for ticker, price in tracker.get_top_10():
        print(f"{ticker}: ${price}")

    print("\nRank of TSLA:", tracker.get_rank("TSLA"))
    print("Rank of GOOGL:", tracker.get_rank("GOOGL"))

    print("\nUpdating AAPL price to 3500...")
    tracker.update("AAPL", 3500)

    print("\nTop 10 after update:")
    for ticker, price in tracker.get_top_10():
        print(f"{ticker}: ${price}")

    print("\nRemoving META...")
    tracker.remove("META")

    print("\nTop 10 after removal:")
    for ticker, price in tracker.get_top_10():
        print(f"{ticker}: ${price}")

if __name__ == "__main__":
    main()