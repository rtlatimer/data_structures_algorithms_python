''' Question 1 '''
'''
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.'''

def question1(s,t):
    if s and t: # Check to see if string is empty
        if len(s) >= len(t): # 't' should not be longer than 's'
            for char in range(len(s)): # Count the length of word 's'
                if sorted(t.lower()) == sorted(s.lower()[char:char + len(t)]): # Check and see if a portion of 't' can be found in 's'
                    print "Looking for '" + t + "' in '" + s + "': "
                    return True
    print "Looking for '" + t + "' in '" + s + "': "
    return False


print "*** Question 1 ***"
print ""
print question1('udacity', 'ad') 
# Answer: True
print question1('udaCiTy', 'city') 
# Answer: True
# Edge Case: upper and lower-case letters
print question1('dormitory', 'room') 
# Answer: False
print question1('astronomy', 'moony') 
# Answer: True
print question1('bubble','sort') 
# Answer: False
print question1('bubble','') 
# Answer: False
# Edge Case: Empty input
print question1('bubble','bub') 
# Answer: True
print question1('spongebob', 'bboeg') 
# Answer: True
print ""




''' Question 2 '''
'''
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.'''

def question2(a):
    if len(a) > 2: # Make sure 'a' is longer than 2 characters
        string = a.lower() # Make all letters lower-case
        word = string[0] # First letter
        for char in range(len(string)): # Count length of word
            for char2 in range(0, char): 
                sub = string[char2:char + 1] # Test all portions of letters in the word
                if sub == sub[::-1]: # If one portion is palindrome
                    if len(sub) > len(word): # And it is longer than the current value of 'word'
                        word = sub # Change word to longest value
        if len(word) > 1: # Make sure value is greater than one character
            print "Looking for palindrome in '" + a + "':"
            return word
        else:
            print "Looking for palindrome in '" + a + "':"
            return None
    print "Looking for palindrome in '" + a + "':"
    print "Word not long enough to test."
    return None
    
print "*** Question 2 ***"
print ""
print question2('bubba')
# Answer: bub
print question2('canals')
# Answer: canal
print question2('amanaplanacanalpanamabanana')
# Answer: amanaplanacanalpanama
print question2('')
# Answer: Word not long enough to test.
# Edge Case: Empty input
print question2('robert')
# Answer: None
print question2('udacity')
# Answer: None
print question2('rubberband')
# Answer: bb
print question2('kAyaks')
# Answer: kayak
# Edge Case: upper and lower-case letters
print ""




''' Question 3 '''
'''
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. 
Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)'''

input1 = {'A': [('B', 2)],
		  'B': [('A', 2), ('C', 5)],
		  'C': [('B', 5)]}

input2 = {'A': [('B', 1), ('C', 6), ('D', 9)],
		  'B': [('A', 1), ('C', 2), ('D', 12)],
		  'C': [('A', 6), ('B', 2), ('D', 8)],
		  'D': [('A', 9), ('B', 12),('C', 8)]}

input3 = {'A': [('B', 2), ('C', 1)],
		  'B': [('A', 2), ('D', 4)],
		  'C': [('A', 1), ('D', 2), ('F', 10)],
		  'D': [('B', 4), ('C', 2), ('E', 3), ('F', 6)],
		  'E': [('D', 3), ('F', 4)],
		  'F': [('C', 10), ('E', 4)]}

input4 = {}


def question3(G):
	if len(G) <= 2: # Graph will be same if there are only 2 nodes
		return G
	graph = G
	min_span_tree = {} # Empty dictionary to store answer
	edges = [] # Empty list to store node+edge info
	for node1 in graph: # Parent nodes
		for (node2, edge) in graph[node1]: # Child nodes and edge values
			edges.append((node1,node2,edge)) # Append to edges list
	sorted_edges = sorted(edges, key=lambda x:x[2]) # Kruskal's Algorithm: Sort in order of smallest edge value
	for (node1,node2,edge) in sorted_edges: # Look at all edges
		if node1 not in min_span_tree or node2 not in min_span_tree: # If one or more nodes from an edge is not in min_span_tree
			if node1 in min_span_tree: # If node 1 is in tree, then that means node 2 is not
				min_span_tree[node1].append((node2,edge)) # append node 2 and connecting edge
			else: # If node 1 is not in tree, then add it
				min_span_tree[node1] = [(node2, edge)] # append node1, node2 & edge
			if node2 in min_span_tree: # If node 2 is in tree, then that means node 1 is not
				min_span_tree[node2].append((node1,edge)) # append node 1 and connecting edge
			else: # If node 2 is not in tree, then add it
				min_span_tree[node2] = [(node1,edge)] # append node2, node1 & edge
	return min_span_tree

print "*** Question 3 ***"
print ""
print "Test 1:"
print question3(input1)
# Answer: {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
# Edge Case: Answer is the same as input
print "Test 2:"
print question3(input2)
# Answer: {'A': [('B', 1)], 'C': [('B', 2), ('D', 8)], 'B': [('A', 1), ('C', 2)], 'D': [('C', 8)]}
#     1
#   A---B
#      /
#    2/
#   C---D 
#     8
print "Test 3:"
print question3(input3)
# Answer: {'A': [('C', 1), ('B', 2)], 'C': [('A', 1), ('D', 2)], 'B': [('A', 2)], 
# 		   'E': [('D', 3), ('F', 4)], 'D': [('C', 2), ('E', 3)], 'F': [('E', 4)]}
#
#      B     D
#    2/     /|
#    /     / |
#   A    2/ 3|  F
#    \   /   | /
#    1\ /    |/4
#      C     E
#
print "Test 4:"
print question3(input4)
# Answer: {}
# Edge Case: Empty input
print ""




''' Question 4 '''
'''
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

def question4(T, r, n1, n2):
	if T == None: # Make sure matrix isn't None
		return "Invalid Matrix"
	if r == None or r < 0: # Make sure root is positive and not None
		return "Invalid Root Value"
	if n1 < 0 or n2 < 0 or n1 == None or n2 == None: # Make sure nodes are positive and not None
		return "Invalid Node Values"
	if (n1 > r and n2 < r) or (n1 < r and n2 > r): # If one node is smaller than root & other is bigger than root
		return r # root must be LCA
	node_parents = {} # empty dict to store node parent pairs
	for row in range(len(T)): # count matrix rows
		for col in range(len(T)): # count matrix columns
			if T[row][col] == 1: # For every '1'...
				node_parents[col] = row # That means the row value is the parent of the column val
			elif T[row][col] > 1 or T[row][col] < 0: # Make sure proper values are entered in matrix
				return "Matrix must only display 1s and 0s."
	#print node_parents # for testing
	if (n1 < r and n2 < r) or (n1 > r and n2 > r): # If both nodes are on the same side of root
		possible_lca = [] # empty list to store possible least common ancestor
		for node, parent in node_parents.iteritems(): # Loop over node-parent pairs
			if (node == n1 and parent == n2) or (node == n2 and parent == n1): # Check to see if node 1 is parent of node 2 or vise versa
				return parent
			if parent == r: # if a parent is the root
				possible_lca.append((node,parent)) # append the pair to possible_lca
		if possible_lca[0][0] == n1 and possible_lca[1][0] == n2: # If both nodes connect directly to root...
			return r # ...then root is lca
		elif n1 < r and n2 < r: # if both nodes are less than the root
			lca = possible_lca[0][0] # lca is the left node connected to root
			return lca
		elif n1 > r and n2 > r: # if both nodes are greater than the root
			lca = possible_lca[1][0] # lca is the right node connected to root
			return lca

print "*** Question 4 ***"
print ""
print "Test 1:"
print question4([[0, 0, 0, 0, 0],
				 [1, 0, 1, 0, 0],
				 [0, 0, 0, 0, 0],
				 [0, 1, 0, 0, 1],
				 [0, 0, 0, 0, 0]], 3, 1, 2)
# Answer: 1
#
#        3
#       / \
#      /   \
#    (1)    4
#    / \
#   /   \
#  0     2
#

print "Test 2:"
print question4([[0, 0, 0, 0, 0, 0, 0],
				 [1, 1, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 1, 0, 0, 1, 0],
				 [0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 1, 0, 1],
				 [0, 0, 0, 0, 0, 0, 0]], 3, 0, 1)
# Answer: 1
# 
#        3
#       / \
#      /   \
#    (1)    5
#    / \   / \
#   /   \ /   \
#   0   2 4   6
#

print "Test 3:"
print question4([[0, 0, 0, 0, 0, 0, 0],
				 [1, 1, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 1, 0, 0, 1, 0],
				 [0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 1, 0, 1],
				 [0, 0, 0, 0, 0, 0, 0]], 3, 4, 6)
# Answer: 5
# 
#        3
#       / \
#      /   \
#     1    (5)
#    / \   / \
#   /   \ /   \
#   0   2 4    6
#

print "Test 4:"
print question4([[0, 0, 0, 0, 0, 0, 0, 0],
				 [1, 1, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 1, 0, 0, 1, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 1, 0, 1, 0],
				 [0, 0, 0, 0, 0, 0, 0, 1],
				 [0, 0, 0, 0, 0, 0, 0, 0]], 3, 6, 7)
# Answer: 6
# 
#        3
#       / \
#      /   \
#     1     5
#    / \   / \
#   /   \ /   \
#   0   2 4   (6)
#               \
#                \
#                 7
#

print "Test 5:"
print question4(None, 3, 1, 2)
# Answer: Invalid Matrix
# Edge Case: Matrix is None

print "Test 6:"
print question4([[0, 0, 0, 0, 0],
				 [1, 0, 1, 0, 0],
				 [0, 0, 0, 0, 0],
				 [0, 1, 0, 0, 1],
				 [0, 0, 0, 0, 0]], -1, 1, 2)
# Answer: Invalid Root Value
# Edge Case: Root is negative int

print "Test 7:"
print question4([[0, 0, 0, 0, 0],
				 [1, 0, 1, 0, 0],
				 [0, 0, 0, 0, 0],
				 [0, 1, 0, 0, 1],
				 [0, 0, 0, 0, 0]], 3, 1, None)
# Answer: Invalid Node Values
# Edge Case: Node2 is None

print "Test 8:"
print question4([[0, 0, 0, 0, 0],
				 [1, 0, -1, 0, 0],
				 [0, 0, 0, 2, 0],
				 [0, 1, 0, 0, 1],
				 [0, 0, 0, 0, 0]], 3, 1, 2)
# Answer: Matrix must only display 1s and 0s.
# Edge Case: Matrix contains numbers other than 1 and 0.
print ""




''' Question 5 '''
'''
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. 
Return the value of the node at that position.'''

# inputs: [ll] - first node of a linked-list & [m] - node at mth number from the end
# output: value of the node at mth position from the end 

class Node(object): # create node class
	def __init__(self, data):
		self.data = data
		self.next = None

# Source: https://www.udacity.com/course/technical-interview--ud513
class LinkedList(object): # create LinkedList class
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

def question5(ll, m):
        if ll == None or m == None: # Make sure inputs are not None
            return "Please enter proper inputs."
        current_node = ll # Set current node
        ll_count = 1 # Set base count
        while current_node: # Count length of Linked List
            current_node = current_node.next # Move to next node
            ll_count += 1 # Add 1 to base count every move
        ll_count = ll_count - m # Subtract m from length of list
        mth_count = 1
        current_node = ll
        while mth_count < ll_count: # Count up to m
            current_node = current_node.next
            mth_count += 1
        if current_node and ll_count > 0: # Make sure values are positive
            return current_node.data # Once you get to m, return value
        else:
            return None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.append(n5)

print "*** Question 5 ***"
print ""
print "Test 1:"
print question5(n1,2) 
# Answer: 4
print "Test 2:"
print question5(n1,3) 
# Answer: 3
print "Test 3:"
print question5(None, None) 
# Answer: Please enter proper inputs.
# Edge Case: Empty inputs

n6 = Node(6)
n7 = Node(7)
ll.append(n7)
ll.append(n6)

print "Test 4:"
print question5(n1,2) 
# Answer: 7
print "Test 5:"
print question5(n1,8) 
# Answer: None
# Edge Case: list is only 7 long
print "Test 6:"
print question5(n1,7) 
# Answer: 1
print "Test 7:"
print question5(n1,0) 
# Answer: None
# Edge Case: Can't count to 0




