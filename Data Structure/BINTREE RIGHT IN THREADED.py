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
    
    def dfind_node(self,node,value):
        if node is None:
            return None
        if node.left is not None :
            if node.left.value==value:
                self.emni='L'
                return node
        
        if node.right is not None :
            if node.right.value==value:
                self.emni='R'
                return node
        found=self.dfind_node(node.left,value)
        if found:
            return found
        return self.dfind_node(node.right,value)

            
    def delete_node(self,value):
        if self.root.value==value:
            print("Deleting Root will Create a Forest and Tree will disappear.")
            self.root=None
            return
        #print("Esechi")
        n = self.find_node(self.root,value)
        
        p = self.dfind_node(self.root,n.value)
        
        if self.emni=='L':
            p.left=None
        if self.emni=='R':
            p.right=None
        self.elements.remove(value)
        

    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
            self.elements.append(value)
        else:
            if value in self.elements:
                print("Element already in Tree.")
                return
            parent_value = self.elements[-1]
            position = 'R'
            parent_node = self.find_node(self.root,parent_value)
            if parent_node is None:
                print(f"Parent node {parent_value} not found. Try again.")
            else:
                self._insert(value,parent_node,position)

    def _insert(self,value,node,n):
        if n=='L':
            if node.left is None: 
                node.left=Node(value)
                self.elements.append(value)
            else:
                print("Left is filled with - ",node.left.value)
        elif n=='R':
            if node.right is None:
                node.right=Node(value)
                self.elements.append(value)
            else:
                print("Right is filled with - ",node.right.value)
                   
    def preorder_traversal(self):
        if self.root is not None:
            self._preorder_traversal(self.root)
    # Helper method for in-order traversal
    def _preorder_traversal(self, current_node):
        if current_node:
            print(current_node.value, end=' ')
            self._preorder_traversal(current_node.left)
            self._preorder_traversal(current_node.right)  

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)
    # Helper method for in-order traversal
    def _inorder_traversal(self, current_node):
        if current_node:
            self._inorder_traversal(current_node.left)
            print(current_node.value, end=' ')
            self._inorder_traversal(current_node.right)  

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)
    # Helper method for in-order traversal
    def _postorder_traversal(self, current_node):
        if current_node:
            self._postorder_traversal(current_node.left)
            self._postorder_traversal(current_node.right)
            print(current_node.value, end=' ')             

a=BinTree()
while True:
    p=input("""1.Insert Node.
2.Pre-Order.
3.In-Order.
4.Post-Order.
5.Delete Node.
6.Exit.
""")
    
    match p:
        case '1':
            v=input("Enter Element - ")
            a.insert(v)
            a.inorder_traversal()
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
            v=input("Enter Element - ")
            a.delete_node(v)
            #a.inorder_traversal()
            print()
            input()
        case '6':
            break
        case _:
            print("Enter correct Input between 1 - 6")
       
        


        
