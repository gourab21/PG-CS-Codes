class Node: 
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.isThreaded = False

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
            
    def find_nodeS(self,node,value,we):
        if node is None:
            return None
        if node.value==value:
            return node
        if node.left is not None:
            if node.value  in we:
                we.remove(node.value)
            return self.find_nodeS(node.left,value,we)
        if node.value  in we:
            we.remove(node.value)
        if node.right is not None and node.right.value in we:
            return self.find_nodeS(node.right,value,we)


    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
            self.elements.append(value)
        else:
            if value in self.elements:
                print("Element already in Tree.")
                return
            parent_value = input(f"Enter parent value for {value}: ")
            position = input(f"Enter position (L for left, R for right) relative to {parent_value}: ").upper()
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


    def populateQueue(self,root, q): 
            if root == None: return
            if root.left: 
                    self.populateQueue(root.left, q) 
            q.append(root)
            
            if root.right: 
                    self.populateQueue(root.right, q) 
                        
    def createThreadedUtil(self, root, q): 
            if root == None: return
            if root.left: 
                    self.createThreadedUtil(root.left, q) 
            q.pop(0) 
            if root.right: 
                    self.createThreadedUtil(root.right, q) 
            else:
                    if len(q) == 0: root.right = None
                    else: root.right = q[0]
                    root.isThreaded = True
                        
    def createThreaded(self): 
            q = [] 
            self.populateQueue(self.root, q) 
            self.createThreadedUtil(self.root, q) 
                
    def leftMost(self,root): 
            while root != None and root.left != None: 
                    root = root.left 
            return root 
        
    def inOrder(self): 
            if self.root == None: return
            cur = self.leftMost(self.root) 
            while cur != None:
                    print(cur.value, end = " ") 
                    if cur.isThreaded: 
                            cur = cur.right 
                    else: 
                            cur = self.leftMost(cur.right) 

a=BinTree()
for i in range(int(input("Enter no. of Nodes - "))):
    a.insert(input("Enter Node - "))

a.createThreaded() 
print("Inorder traversal of created threaded tree is") 
a.inOrder()


while True:
      s=input("Enter element to search - ")
      if s=='-1':
            break
      we=a.elements
      we={}
      s=a.find_nodeS(a.root,s,we)
      if s is None:
            print("Not Found ",s)
      else:
            print("Right Pointer - ",s.right.value)



