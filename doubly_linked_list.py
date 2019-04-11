class DoublyLinkedListNode (object):
    def __init__(self, value):
        self.val = value
        self.next_node = None
        self.prev_node = None


first = DoublyLinkedListNode(1)

second = DoublyLinkedListNode(2)

third = DoublyLinkedListNode(3)

first.next_node = second
second.prev_node = first
second.next_node = third
third.prev_node = second

print(second.val)
