class Node(object):
    def __init__(self, value=None, nextnode=None):
        self.value = value
        self.nextnode = nextnode


a = Node(1)
b = Node(3)
c = Node(4)
d = Node(5)
e = Node(7)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = None


def deleteElement(head, value):

    try:
        current_node = head

        while current_node.nextnode:
            if current_node.nextnode.value == value:
                next_to_next_node = current_node.nextnode.nextnode
                current_node.nextnode = None
                current_node.nextnode = next_to_next_node
                return True
            current_node = current_node.nextnode

        return False
    except Exception as er:
        print(er)


x = deleteElement(a, 6)

if x:
    print("Element was deleted")
else:
    print("Element not found")
