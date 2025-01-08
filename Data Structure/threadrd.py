
# Python3 program to convert 
# a Binary Tree to Threaded Tree

# Structure of a node in threaded binary tree 
class Node: 

	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		
		# Used to indicate whether the right pointer 
		# is a normal right pointer or a pointer to
		# inorder successor. 
		self.isThreaded = False

# Helper function to put the Nodes 
# in inorder into queue 
def populateQueue(root, q): 

	if root == None: return
	if root.left: 
		populateQueue(root.left, q) 
	q.append(root)
	
	if root.right: 
		populateQueue(root.right, q) 

# Function to traverse queue, 
# and make tree threaded 
def createThreadedUtil(root, q): 

	if root == None: return

	if root.left: 
		createThreadedUtil(root.left, q) 
	q.pop(0) 

	if root.right: 
		createThreadedUtil(root.right, q) 

	# If right pointer is None, link it to the 
	# inorder successor and set 'isThreaded' bit. 
	else:
		if len(q) == 0: root.right = None
		else: root.right = q[0]
		root.isThreaded = True

# This function uses populateQueue() and 
# createThreadedUtil() to convert a given 
# binary tree to threaded tree. 
def createThreaded(root): 

	# Create a queue to store inorder traversal 
	q = [] 

	# Store inorder traversal in queue 
	populateQueue(root, q) 

	# Link None right pointers to inorder successor 
	createThreadedUtil(root, q) 

# A utility function to find leftmost node 
# in a binary tree rooted with 'root'. 
# This function is used in inOrder() 
def leftMost(root): 

	while root != None and root.left != None: 
		root = root.left 
	return root 

# Function to do inorder traversal 
# of a threaded binary tree 
def inOrder(root): 

	if root == None: return

	# Find the leftmost node in Binary Tree 
	cur = leftMost(root) 

	while cur != None:
	
		print(cur.key, end = " ") 

		# If this Node is a thread Node, 
		# then go to inorder successor 
		if cur.isThreaded: 
			cur = cur.right 

		# Else go to the leftmost child 
		# in right subtree 
		else: 
			cur = leftMost(cur.right) 
	
# Driver Code
if __name__ == "__main__":

	root = Node(1) 
	root.left = Node(2) 
	root.right = Node(3) 
	root.left.left = Node(4) 
	root.left.right = Node(5) 
	root.right.left = Node(6) 
	root.right.right = Node(7) 

	createThreaded(root) 

	print("Inorder traversal of created threaded tree is") 
	inOrder(root) 
	
# This code is contributed by Rituraj Jain
