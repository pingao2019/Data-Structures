"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # compare the value to the root's value to determine which direction
        # we're gonna go in 
        # if the value < root's value 
        if value < self.value:
            # go left 
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left: 
                # then self.left is a Node 
                # now what?
                self.left.insert(value)
            else: # no self.left node
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's value 
        else:
            # go right
            # how do we go right? 
            # we have to check if there is another node on the right side 
            if self.right:
                # then self.right is a Node 
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    
            # Return True if the tree contains the value
        # False if it does not
    def contains(self, target):

	    # base case?
	    # we find the target in a tree node 
	    if self.value == target:
			return True
	    # figure out which direction we need to go in 
	    if target < self.value:
		    # we go left 
		    if not self.left:
			    return False
		    else:
			    return self.left.contains(target)
		# or, we get to a spot where the node should be, but nothing is there 
		# how do we move towards the base case? 
		    else:
			# we go right 
			    if not self.right:
				    return False
			    else:
				return self.right.contains(target)

	def get_max(self):
		# we can just keep going right until we can't go right anymore 
		if not self.right:
			return self.value
		return self.right.get_max()

			# Call the function `fn` on the value of each node
			# doesn't actually return anything 
     
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

	def depth_first_for_each(self, fn):
				# this method specifically does want to traverse every tree node 
				# this has to call the fn on self.value 
				fn(self.value)

				# how do we propagate to all the other nodes in the tree? 
				# is there a left child? 
				if self.left:
					# if yes, then call its `for_each` with the same fn 
					self.left.depth_first_for_each(fn)
					# is there a right child?
					if self.right:
						# if yes, then call its `for_each` with the same fn 
						self.right.depth_first_for_each(fn)

	def iter_depth_first_for_each(self, fn):
							# with depth-first traversal, there's a certain order to when we visit nodes 
		# what's that order? 
		# init a stack to keep track of the order of nodes we visited 
		stack = []
							# add the first node to our stack 
		stack.append(self)
							# continue traversing until our stack is empty
		while len(stack) > 0: 
			# pop off the stack 
			current_node = stack.pop()
								# add its children to the stack 
								# add the right child first and left child second
								# to ensure that left is popped off the stack first 
			if current_node.right:
				stack.append(current_node.right)
				if current_node.left:
					stack.append(current_node.left)
										# call the fn function on self.value 
					fn(self.value)

	def iter_breadth_first_search(self, fn):
											# breadth first traversal follows FIFO ordering of its nodes
											# init a deque 
		q = deque()
											# add the first node to our q 
		q.append(self)

		while len(q) > 0:
			current_node = q.popleft()
			if current_node.left:
				q.append(current_node.left)
				if current_node.right:
					q.append(current_node.right)
					fn(self.value)
   
	
        

    
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    
    def in_order_print(self, node):
        if node.left:
			self.in_order_print(node.left)
            print(node.value)
        if node.right:
            self.in_order_print(node.right)
			print(node.value)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #using queue

		q = deque()
		# add the first node to our q 
		q.append(self)

		while len(q) > 0:
			current_node = q.popleft()
			if current_node.left:
				q.append(current_node.left)
				if current_node.right:
					q.append(current_node.right)
					print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # using stack
        stack = []
							 
		stack.append(self)
							 
		while len(stack) > 0: 
			# pop off the stack 
			current_node = stack.pop()
								# add its children to the stack 
								# add the right child first and left child second
								# to ensure that left is popped off the stack first 
			if current_node.right:
				stack.append(current_node.right)
				if current_node.left:
					stack.append(current_node.left)
										# call the fn function on self.value 
					print(current_node.value))


        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
	# reference:https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            node.left.pre_order_dft(node.left)
        if node.right is not None:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if node.left is not None:
            self.left.post_order_dft(node.left)
        if node.right is not None:
            self.right.post_order_dft(node.right)
        print(node.value)
