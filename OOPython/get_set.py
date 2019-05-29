class kv:
    def __init__(self, k=None, v=None):
        self.store = {k: v}

    def set(self, k, v):
        self.store[k] = v

    def get(self, k):
        return self.store[k]


new_kv = kv()

new_kv.set("b", "ball")
print(new_kv.get("b"))
