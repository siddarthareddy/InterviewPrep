# O(n^2) O(n) O(1)
# O(nlogn) O(log(n))

#Recursive Algorithm
#Time - avg O(log(n)) time | worst case O(n)
#Space - avg O(log(n)) time | worst case O(n) - n recursive calls

#Iterative Algorithm
#Space - O(1) time - avg & worst case
from random import randrange
from treeUtil import Node, insert

def findClosestValueBstR(tree, target):
    return findClosestValueBstHelperR(tree, target, float("inf"))

def findClosestValueBstHelperR(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueBstHelperR(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueBstHelperR(tree.right, target, closest)
    else:
        return closest


def findClosestValueBstI(tree, target):
    return findClosestValueBstHelperI(tree, target, float("inf"))

def findClosestValueBstHelperI(tree, target, closest):
    currentNode = tree
    while currentNode is not  None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > tree.value:
            currentNode = currentNode.right
        else:
            break

    return closest

def testR():
    print(findClosestValueBstR(r, 5000))

def testI():
    print(findClosestValueBstI(r, 12345))

if __name__ == '__main__':
    r = Node(50)
    for i in range(1, 100000):
        insert(r, Node(randrange(1000000000)))

    testI()