# O(n^2) O(n) O(1)
# O(nlogn) O(log(n))

#DFS - as we traverse grab the nodes and put them in array
#space time complexity is a bit involved
# coz there are vertices and edges v, e
# Time - O(V+E) - more edges more time
# Space O(V) - coz there can be V frames on call stack, also V nodes to store

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def dFS(self, array):
        array.append(self.name)
        for child in self.children:
            child.dFS(array)
        return array

if __name__ == '__main__':
    r1 = Node(50)
    r2 = Node(20)
    r3 = Node(10)
    r1.addChild(r2)
    r2.addChild(r3)
    r4 = Node(5)
    r1.addChild(r4)

    print( r2.dFS([]))
