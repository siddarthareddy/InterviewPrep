#Time - O(nd)
#Space - O(n)
def minCoinsForChange(denoms, amt):
    min = [0 for amount in range(amt+1)]
    min[0] = 0
    for coin in denoms:
        if coin <= amt:
            min[coin] = 1
    for i in range(1,amt+1):
        for denom in denoms:
            if i >= denom:
                min[i] = min[i-denom] + 1
    return min[amt]

def minCoinsForChange2(denoms, n):
    numOfCoins = [float("inf") for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                numOfCoins[amount]= min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
    return numOfCoins[n] if numOfCoins[n] != float("inf") else - 1


if __name__ == "__main__":
    a = [1, 2, 4]
    print(minCoinsForChange(a, 6))
    print(minCoinsForChange2(a, 6))
    a = [5,10]
    print(minCoinsForChange(a, 100))

