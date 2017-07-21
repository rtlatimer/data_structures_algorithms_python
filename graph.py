class Node(object): # building blocks
	def __init__(self, value):
		self.value = value # Each node has some value
		self.edges = [] # and a list of edges

class Edge(object): # connecting link between nodes
	def __init__(self, value, node_from, node_to):
		self.value = value # edge can have a value
		self.node_from = node_from # and a direction to, from, or both
		self.node_to = node_to

class Graph(object): # Graph is made up of nodes and edges
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges

	def insert_node(self, new_node_val): # Method used to add a node to a graph
		new_node = Node(new_node_val)
		self.nodes.append(new_node)

	def insert_edge(self, new_edge_val, node_from_val, node_to_val): # inserts a new edge to graph
		from_found = None # default variables
		to_found = None
		for node in self.nodes: # for all of the nodes
			if node_from_val == node.value: # look for one that matches node_from_val
				from_found = node # update from_found variable
			if node_to_val == node.value: # look for one that matches node_to_val
				to_found = node # update to_found variable
		if from_found == None: # If no nodes match node_from_val
			from_found = Node(node_from_val) # make a new node
			self.nodes.append(from_found) # add it to the list of nodes
		if to_found == None: # If no nodes match node_to_val
			to_found = Node(node_to_val) # make new node
			self.nodes.append(to_found) # add to node list
		new_edge = Edge(new_edge_val, from_found, to_found) # make a new edge connecting from_found & to_found
		from_found.edges.append(new_edge) # append edge to from_found
		to_found.edges.append(new_edge) # and to_found
		self.edges.append(new_edge) # append edge to edge list

	def get_edge_list(self):
		# return a list of triples like this (Edge Value, From Node Value, To Node Value)
		edge_list = []
		for edge_object in self.edges:
			edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
			edge_list.append(edge)
		return edge_list

	def get_adjacency_list(self):
		max_index = self.find_max_index()
		adjacency_list = [None] * (max_index + 1)
		for edge_object in self.edges:
			if adjacency_list[edge_object.node_from.value]:
				adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
			else:
				adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
		return adjacency_list
		# return list of lists
		# outer list represents "from" nodes and inner list is (To Node, Edge Value)


	def get_adjacency_matrix(self):
		# return a matrix where rows are "from" nodes, columns are "to" nodes
		# edge values in each spot & 0 if no edge
		max_index = self.find_max_index()
		adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
		for edge_object in self.edges:
			adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
		return adjacency_matrix

	def find_max_index(self):
		max_index = -1
		if len(self.nodes):
			for node in self.nodes:
				if node.value > max_index:
					max_index = node.value
		return max_index



graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print graph.get_edge_list()
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()

