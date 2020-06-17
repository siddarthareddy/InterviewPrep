# generate random integer values
from random import seed
from random import randint
# generate some integers


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def setNext(self, mext):
        self.next = next

#Time - O(size_of_list)
#Space = O(1)
def nFrmEnd(head, n):
    # before writing all this code, ask interviwer for sensible assumptions
    #like min size of list be n, else makes life harder
    # if node is None:
    #     return
    # front = node
    #
    # while front.next is not None and n <= 1:
    #     front = front.next
    #     n -= 1
    # if n > 1:
    #     return
    counter = 1
    first = head
    second = head
    while counter <= n:
        second = second.next
        counter += 1
    #now second node is n nodes ahead
    if second is None:
        #head = head.next
        # that is wrong,
        # reference outside the fuction which is passed down
        # still refers to original head, as it was never changes,
        # a copy of the reference is change(pass-by-value)
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
    #
    # for i in range(n-1):
    #     second = second.next
    # if second == None:
    #     head = head.next
    # else:
    #     second = second.next
    #     if second is None:
    #         head = head.next
    #         return
    #     while second is not None:
    #         first = first.next
    #         second = second.next
    #     first.next = first.next.next

def printList(head):
    arr = []
    node = head
    while node != None:
        arr.append(node.value)
        node = node.next
    print(arr)

if __name__ == "__main__":
    head = Node(10)
    current = head
    # seed random number generator
    seed(1)
    for i in range(10):
        value = randint(0, 10)
        current.next = Node(value)
        current = current.next
    printList(head)
    nFrmEnd(head, 1)
    printList(head)
    nFrmEnd(head, 5)
    printList(head)
    nFrmEnd(head, 9)
    printList(head)


