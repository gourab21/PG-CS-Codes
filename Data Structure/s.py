# Define a class for a node in the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define a class for the binary tree
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node into the binary tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    # Helper method to insert a node in the correct place
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)

    # Search for a value in the binary tree
    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    # Helper method to search for a value
    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left:
            return self._search(value, current_node.left)
        elif value > current_node.value and current_node.right:
            return self._search(value, current_node.right)
        return False

    # In-order traversal (left-root-right)
    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    # Helper method for in-order traversal
    def _inorder_traversal(self, current_node):
        if current_node:
            self._inorder_traversal(current_node.left)
            print(current_node.value, end=' ')
            self._inorder_traversal(current_node.right)

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)

    print("In-order traversal:")
    tree.inorder_traversal()  # Output: 2 5 7 10 15

    print("\nSearch for 7:", tree.search(7))  # Output: True
    print("Search for 20:", tree.search(20))  # Output: False
