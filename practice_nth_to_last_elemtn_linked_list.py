#  The goal is to find the nth to the last element in a linked list
# nth_to_the_last_node(a, n)


class Node(object):
    def __init__(self, value=None, nextnode=None):
        self.value = value
        self.nextnode = nextnode


# Creating a few nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
f.nextnode = None


def nth_element_from_last(n, a):
    try:
        current = a
        nth_from_last = a

        for i in range(0, n):
            current = current.nextnode

        if current == None:
            return None
        else:
            while current.nextnode:
                current = current.nextnode
                nth_from_last = nth_from_last.nextnode

        return(nth_from_last)
    except Exception as err:
        return None


nth_element_from_last = nth_element_from_last(5, a)

if nth_element_from_last:
    print(nth_element_from_last.value)
else:
    print("n was too large")
