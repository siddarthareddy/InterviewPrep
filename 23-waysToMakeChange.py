#Time - O(nd)
#Space - O(n)
def waysToMakeChange(denoms, amt):
    ways = [0 for amount in range(amt+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, amt+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[amt]

if __name__ == "__main__":
    a = [1,5,10,25]
    print(waysToMakeChange(a, 10))
    a = [5,10]
    print(waysToMakeChange(a, 9))
    print(waysToMakeChange(a, 100))
