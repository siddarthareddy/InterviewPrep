# recursive Time - O(2^n)  | Space - O(n)

def nthFibonacciRec(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return nthFibonacciRec(n-1) + nthFibonacciRec(n-2)

#memoize Time - O(n) | Space - O(n)
def nthFibonacciMemoize(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = nthFibonacciMemoize(n - 1, memoize) + nthFibonacciMemoize(n - 2, memoize)
        return memoize[n]

#Iterative - Time - O(n) | Space - O(1)
def nthFibonacciIter(n):
    arr = [0,1]
    i = 1
    while i < n:
        next = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = next
        i += 1
    return arr[-1] if n > 1 else arr[0]

if __name__ == "__main__":
    print(nthFibonacciMemoize(5))