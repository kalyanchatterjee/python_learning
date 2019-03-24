from collections import deque

# class collections.deque([iterable[, maxlen]])
# Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.

# Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# As long as queue has elements, keep popping elements
while queue:
    queue.popleft()
    print(queue)

if not queue:
    print("empty")
