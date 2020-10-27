import math
def findOptimal(mat):
    print(optimal(mat, 0, len(mat)-1))


def optimal(mat, start, end, cache={}):
    if (start, end) in cache:
        return cache[(start, end)]
    opt = math.inf
    if start == end:
        cache[(start, end)] = 0
        return 0
    if end == start+1:
        cache[(start, end)] = mat[start][0]*mat[start][1]*mat[end][1]
        return cache[(start, end)]

    for i in range(start, end):
        a = optimal(mat, start, i)
        b = optimal(mat, i+1, end)
        c = mat[start][0]*mat[i][1]*mat[end][1]
        opt = min(opt, a+b+c)
    cache[(start, end)] = opt
    return opt

arr = [(2,10),(10,3),(3,8)]
findOptimal(arr)