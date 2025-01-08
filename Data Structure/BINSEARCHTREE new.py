class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinTree:
    def __init__(self):
        self.root=None
        self.elements=[]
        self.emni=''

    def find_node(self,node,value):
        if node is None:
            return None
        if node.value==value:
            return node
        found=self.find_node(node.left,value)
        if found:
            return found
        return self.find_node(node.right,value)
         
    def insert(self, value):
        """Inserts a new node with the given value into the BST."""
        if self.root is None:
            self.root = Node(value)
            self.elements.append(value)
        elif value in self.elements:
            print("Element already in Tree.")
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if int(value) < int(root.value):
            if root.left is None:
                print(root.value,"  L")
                root.left = Node(value)
                self.elements.append(value)
            else:
                self._insert(root.left, value)
        elif int(value) > int(root.value):
            if root.right is None:
                print(root.value,"  R")
                root.right = Node(value)
                self.elements.append(value)
            else:
                self._insert(root.right, value)
                   
    def preorder_traversal(self):
        if self.root is not None:
            print("Preorder Traversal - ",end=" ")
            self._preorder_traversal(self.root)
    # Helper method for in-order traversal
    def _preorder_traversal(self, current_node):
        if current_node:
            print(current_node.value, end=' ')
            self._preorder_traversal(current_node.left)
            self._preorder_traversal(current_node.right)  

    def inorder_traversal(self):
        if self.root is not None:
            print("Inorder Traversal - ",end=" ")
            self._inorder_traversal(self.root)
    # Helper method for in-order traversal
    def _inorder_traversal(self, current_node):
        if current_node:
            self._inorder_traversal(current_node.left)
            print(current_node.value, end=' ')
            self._inorder_traversal(current_node.right)  

    def postorder_traversal(self):
        if self.root is not None:
            print("Postorder Traversal - ",end=" ")
            self._postorder_traversal(self.root)
    # Helper method for in-order traversal
    def _postorder_traversal(self, current_node):
        if current_node:
            self._postorder_traversal(current_node.left)
            self._postorder_traversal(current_node.right)
            print(current_node.value, end=' ')            

a=BinTree()
while True:
    try:
        p=input("""1.Insert Node.
2.Pre-Order.
3.In-Order.
4.Post-Order.
5.Exit.
Enter Your Choice   -   """)

        match p:
            case '1':
                v=input("Enter Element - ")
                a.insert(v)
                #a.inorder_traversal()
                print()
            case '2':
                a.preorder_traversal()
                print()
            case '3':
                a.inorder_traversal()
                print()
            case '4':
                a.postorder_traversal()
                print()
            case '5':
                break
            case _:
                print("Enter correct Input between 1 - 6")
    except Exception as e:
        print("Error Occured. ",e)