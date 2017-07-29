'''Question 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
For example, the root is a common ancestor of all nodes on the tree, 
but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), 
where T is the tree represented as a matrix, 
where the index of the list is equal to the integer stored in that node and a 1 represents a child node, 
r is a non-negative integer representing the root, 
and n1 and n2 are non-negative integers representing the two nodes in no particular order. 
For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.'''


# Question 4
def question4(T, r, n1, n2):
	if (n1 > r and n2 < r) or (n1 < r and n2 > r):
		return r
	node_parents = {}
	for row in range(len(T)):
		for col in range(len(T)):
			if T[row][col] == 1:
				node_parents[col] = row
			elif T[row][col] > 1 or T[row][col] < 0:
				return "Matrix must only display 1s and 0s."
	print node_parents
	if (n1 < r and n2 < r) or (n1 > r and n2 > r):
		possible_lca = []
		for node, parent in node_parents.iteritems():
			if parent == r:
				possible_lca.append((node,parent))
		if possible_lca[0][0] == n1 and possible_lca[1][0] == n2:
			return r
		elif n1 < r and n2 < r:
			lca = possible_lca[0][0]
			return lca
		elif n1 > r and n2 > r:
			lca = possible_lca[1][0]
			return lca



print question4([[0, 0, 0, 0, 0],
				 [1, 0, 1, 0, 0],
				 [0, 0, 0, 0, 0],
				 [0, 1, 0, 0, 1],
				 [0, 0, 0, 0, 0]], 3, 1, 2)

print question4([[0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0],
				 [1, 1, 0, 0, 0, 0, 0],
				 [0, 0, 1, 0, 0, 1, 0],
				 [0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 1, 0, 1],
				 [0, 0, 0, 0, 0, 0, 0]], 3, 0, 1)
