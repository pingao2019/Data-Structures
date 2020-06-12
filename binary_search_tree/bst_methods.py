# Return True if the tree contains the value
# False if it does not
def contains(self, target):
	# base case?
	# we find the target in a tree node 
	if self.value == target:
		return True
	else:
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

			# Return the maximum value found in the tree
			def get_max(self):
				# we can just keep going right until we can't go right anymore 
				if not self.right:
					return self.value
				return self.right.get_max()

			# Call the function `fn` on the value of each node
			# doesn't actually return anything 
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