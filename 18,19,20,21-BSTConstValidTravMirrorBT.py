from treeUtil import print_tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Time - Avg Case - O(log n)
    # Time - Worst case - O(n)
    # Space - Avg Case - O(1)
    # Space - Worst case - O(1)
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    #new currentNode is smallest value of right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def remove1(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    #new currentNode is smallest value of right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                elif currentNode.left is not None:
                    currentNode.value = currentNode.left.getMaxValue()
                    currentNode.left.remove(currentNode.value, currentNode)
                else:
                    if parentNode.left == currentNode:
                        parentNode.left = None
                    elif parentNode.right == currentNode:
                        parentNode.right = None
                break
        return self


    def remove2(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    #new currentNode is smallest value of right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                elif currentNode.right is not None:
                    if parentNode.left == currentNode:
                        parentNode.left = currentNode.right
                    else:
                        parentNode.right = currentNode.right
                elif currentNode.left is not None:
                    if parentNode.left == currentNode:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.right = currentNode.left
                else:
                    if parentNode.left == currentNode:
                        parentNode.left = None
                    elif parentNode.right == currentNode:
                        parentNode.right = None
                break
        return self

    def getMinValue(self, minValue=float("inf")):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def getMaxValue(self):
        currentNode = self
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.value

    def mirrorBTRecursive(self):
        if self is None:
            return
        else:
            self.right, self.left = self.left, self.right
            self.left.mirrorBTRecursive() if self.left is not None else None
            self.right.mirrorBTRecursive() if self.right is not None else None
        return self



#Time - O(nlog(n)), obvious method
# Space - O(d) - depth of the tree
def validateBSTBruteForce(node):
    if node is None:
        return True
    elif node.left is not None and node.right is not None:
        if node.left.getMaxValue() < node.value and node.value <= node.right.getMinValue():
            return validateBSTBruteForce(node.left) and validateBSTBruteForce(node.right)
        else:
            return False
    elif node.left is not None:
        if node.left.getMaxValue() < node.value:
            return validateBSTBruteForce(node.left)
        else:
            return False
    elif node.right is not None:
        if node.right.getMinValue() >= node.value:
            return validateBSTBruteForce(node.right)
        else:
            return False
    else:
        return True

#Time - O(n)
#Space - O(d)
def validateBSTOptimised(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
    rightIsValid = validateBSTHelper(tree.right, tree.value, maxValue)
    return leftIsValid and rightIsValid

# Time - O(n), Space - O(d) - if array is not needed, but print
def traverseInOrder(node, array):
    if node is None:
        return array
    traverseInOrder(node.left, array)
    array.append(node.value)
    traverseInOrder(node.right, array)
    return array

def traversePreOrder(node, array):
    if node is None:
        return array
    array.append(node.value)
    traversePreOrder(node.left, array)
    traversePreOrder(node.right, array)
    return array

def traversePostOrder(node, array):
    if node is None:
        return array
    traversePostOrder(node.left, array)
    traversePostOrder(node.right, array)
    array.append(node.value)
    return array

#Time - O(n)
#Space - O(n)
def mirrorBTBFS(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

#Time - O(n)
#Space - O(d)
def mirrorBTRec(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    mirrorBTRec(tree.left)
    mirrorBTRec(tree.right)

if __name__ == "__main__":
    a = [5, 5, 2, 1, 15, 22, 21, 16, 8, 1, 7, 6, 3]
    root = BST(10)
    for i in a:
        root.insert(i)
    print_tree(root)
    print_tree(root.remove(10))
    print_tree(root.remove(1))
    print_tree(root.remove2(8))
    # root.insert(10)
    print(validateBSTBruteForce(root))
    print_tree(root.mirrorBTRecursive())
    mirrorBTRec(root)
    print_tree(root)
    print(validateBSTOptimised(root))
    print(traverseInOrder(root, []))
    print(traversePreOrder(root, []))
    print(traversePostOrder(root, []))

