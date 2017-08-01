'''Question 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. 
Return the value of the node at that position.'''

# inputs: [ll] - first node of a linked-list & [m] - node at mth number from the end
# output: value of the node at mth position from the end 

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
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
        if ll == None or m == None:
            return "Please enter proper inputs."
        current_node = ll
        ll_count = 1
        while current_node:
            current_node = current_node.next
            ll_count += 1
        ll_count = ll_count - m
        mth_count = 1
        current_node = ll
        while mth_count < ll_count:
            current_node = current_node.next
            mth_count += 1
        if current_node and ll_count > 0:
            return current_node.data
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

print question5(n1,2) # Answer: 4
print question5(n1,3) # Answer: 3
print question5(None, None) # Answer: Please enter proper inputs.

n6 = Node(6)
n7 = Node(7)
ll.append(n6)
ll.append(n7)

print question5(n1,2) # Answer: 6
print question5(n1,8) # Answer: None
print question5(n1,7) # Answer: 1
print question5(n1,0) # Answer: None


        