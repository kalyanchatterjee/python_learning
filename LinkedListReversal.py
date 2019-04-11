class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def reverse(head):
    if head.next == None:
        return head
    else:
        current = head
        nextnode = None
        prevnode = None

        while current:
            nextnode = current.next
            current.next = prevnode
            prevnode = current
            current = nextnode


if __name__ == "__main__":

    a = Node(value=1)
    b = Node(value=2)
    c = Node(value=3)

    a.next = b
    b.next = c
    c.next = None

    print(a.next.value)
    print(b.next.value)

    reverse(a)

    print("List reversed:")
    print(c.next.value)
    print(b.next.value)
