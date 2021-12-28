class node:

    def __init__(self, n):
        self.id = n
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' position: ' + str([p.id for p in self.adjacent])

