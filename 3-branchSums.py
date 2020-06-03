# O(n^2) O(n) O(1)
# O(nlogn) O(log(n))

from random import randrange
from treeUtil import Node, insert, print_tree

# Time O(n)
# Space O(n) (no. of leaf nodes)
def branchSums(tree):
    array = []
    branchSumHelper(tree, 0, array)
    print(array)

def branchSumHelper(tree, sum, array):
    if tree is None:
        return
    sum = sum + tree.value
    if tree.left is None and tree.right is None:
        array.append(sum)
    branchSumHelper(tree.left, sum, array)
    branchSumHelper(tree.right, sum, array)

if __name__ == '__main__':
    import timeit
    r = Node(5)
    
    for i in range(1, 20):
        insert(r, Node(randrange(5)))
    print_tree(r)
    branchSums(r)