def getPermutations1(array):
    permutations = []
    permutationsHelper(array, [])
    return permutations

def permutationsHelper(array, currentPermutation):
    if not len(array) and len(currentPermutation):
        # permutations.append(currentPermutation)
        print(currentPermutation)
    else:
        for i in range(len(array)):
            a = array.pop(i)
            currentPermutation.append(a)
            permutationsHelper(array, currentPermutation)
            currentPermutation.pop()
            #Time- O(n) operation
            array.insert(i, a)

            # O(n) time
            # newArray = array[:i] + array[i+1:]
            # newPermutation = currentPermutation + [array[i]]
            # permutationsHelper(newArray, newPermutation)


def permutations(array):
    permutationsA(array, 0)

def permutationsA(array, n):
    if n == len(array) - 1:
        print(array)
        return
    for i in range(n, len(array)):
        swap(array, n, i)
        permutationsA(array, n+1)
        swap(array, n, i)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    permutations([1,2,3])
    print("***")
    getPermutations1([1,2,3])