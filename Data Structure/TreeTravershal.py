class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to perform inorder traversal
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end=" ")
        inorderTraversal(root.right)


# Function to perform preorder traversal
def preorderTraversal(root):
    if root:
        print(root.data, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)


# Function to perform postorder traversal
def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data, end=" ")


# Function to insert nodes into the binary tree
def insert_node(parent, value, position):
    if position == 'L':
        if parent.left is None:
            parent.left = Node(value)
        else:
            print(f"Left child of {parent.data} is already filled.")
    elif position == 'R':
        if parent.right is None:
            parent.right = Node(value)
        else:
            print(f"Right child of {parent.data} is already filled.")


# Function to find a node by value
def find_node(root, value):
    if root is None:
        return None
    if root.data == value:
        return root
    found = find_node(root.left, value)
    if found is None:
        found = find_node(root.right, value)
    return found


# Main driver code
if __name__ == '__main__':
    try:
        root = None
        while True:
            print("\nMenu:")
            print("1. Insert node")
            print("2. Inorder Traversal")
            print("3. Preorder Traversal")
            print("4. Postorder Traversal")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if root is None:
                    root_value = input("Enter the value for the root node: ")
                    root = Node(root_value)
                else:
                    value = input("Enter new node value: ")
                    parent_value = input(f"Enter parent value for {value}: ")
                    position = input(f"Enter position (L for left, R for right) relative to {parent_value}: ").upper()

                    parent_node = find_node(root, parent_value)
                    if parent_node is None:
                        print(f"Parent node {parent_value} not found. Try again.")
                    else:
                        insert_node(parent_node, value, position)

            elif choice == 2:
                if root is None:
                    print("Tree is empty. Please insert any node.")
                else:
                    print("Inorder traversal of the binary tree is:")
                    inorderTraversal(root)
                    print()

            elif choice == 3:
                if root is None:
                    print("Tree is empty. Please insert any node.")
                else:
                    print("Preorder traversal of the binary tree is:")
                    preorderTraversal(root)
                    print()

            elif choice == 4:
                if root is None:
                    print("Tree is empty. Please insert any node.")
                else:
                    print("Postorder traversal of the binary tree is:")
                    postorderTraversal(root)
                    print()

            elif choice == 5:
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please try again.")

    except ValueError:
        print("Invalid input! Please enter numeric(1 to 5) values for choices.")
