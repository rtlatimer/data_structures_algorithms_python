'''Question 3
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
	if len(G) <= 2:
		return G
	graph = G
	min_span_tree = {}
	edges = []
	for node1 in graph:
		for (node2, edge) in graph[node1]:
			edges.append((node1,node2,edge))
	sorted_edges = sorted(edges, key=lambda x:x[2])
	for (node1,node2,edge) in sorted_edges:
		if node1 not in min_span_tree or node2 not in min_span_tree:
			if node1 in min_span_tree:
				min_span_tree[node1].append((node2,edge))
			else:
				min_span_tree[node1] = [(node2, edge)]
			if node2 in min_span_tree:
				min_span_tree[node2].append((node1,edge))
			else:
				min_span_tree[node2] = [(node1,edge)]
	return min_span_tree

print question3(input1)
print question3(input2)
print question3(input3)
print question3(input4)




