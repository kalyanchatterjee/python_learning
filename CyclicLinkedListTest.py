# Given a single linked list, check if it is cyclic.

# If a linked list is cyclic is means, the next pointer
# of a node, points back to a prev node

# You're given the following

import sys


class LinkedListNode (object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Traverse the list and check if any node points back to
# a node already been traversed.


a = LinkedListNode(value=2)
b = LinkedListNode(value=4)
c = LinkedListNode(value=5)

a.next = b
b.next = c
c.next = a

start_node = a

if start_node.next is None:
    exit
else:
    # Add current Node to list nodes_traversed
    nodes_traversed = [start_node]
    next_node = start_node.next
    while next_node:
        if next_node.next in nodes_traversed:
            print("Cyclic LL")
            sys.exit()
        else:
            nodes_traversed.append(next_node)
            next_node = next_node.next
    print("Not a Cyclic LL")
