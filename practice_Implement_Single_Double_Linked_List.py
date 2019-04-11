class Single(object):
    def __init__(self, value=None, nextnode=None):
        self.value = value
        self.nextnode = nextnode


class Double(object):
    def __init__(self, value=None, prevnode=None, nextnode=None):
        self.value = value
        self.prevnode = prevnode
        self.nextnode = nextnode


a = Single(1)
b = Single(2)
c = Single(3)

a.nextnode = b
b.nextnode = c
c.nextnode = None

d = Double(4)
e = Double(5)
f = Double(6)

d.nextnode = e
d.prevnode = None
e.nextnode = f
e.prevnode = d
f.nextnode = None
f.prevnode = e

print(a.nextnode.value)
print(e.prevnode.value)
