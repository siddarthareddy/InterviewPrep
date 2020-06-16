#Time - O(nd)
#Space - O(n)
def minCoinsForChange(denoms, amt):
    min = [float("inf") for amount in range(amt+1)]
    min[0] = 0
    for amount in range(1,amt+1):
        for denom in denoms:
            if denom <= amount:
                min[amount] = mininum(min[amount - denom] + 1, min[amount])
    return min[amt]

def minCoinsForChange2(denoms, n):
    numOfCoins = [float("inf") for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                numOfCoins[amount]= min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
    return numOfCoins[n] if numOfCoins[n] != float("inf") else - 1

def mininum(a, b):
    return a if a < b else b
if __name__ == "__main__":
    a = [1, 2, 4]
    print(minCoinsForChange(a, 6))
    print(minCoinsForChange2(a, 6))
    a = [1]
    print(minCoinsForChange(a, 100))

