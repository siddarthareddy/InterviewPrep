class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    #O(V+E) time - this is clear when it's a graph instead of a tree
    # in case of graph, we have to check if the child node
    # is visited already before enqueing
    # This helps with loops on the graph

    #O(V) space
    def bFS(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current)
            for child in current.children:
                queue.append(child)
        return array