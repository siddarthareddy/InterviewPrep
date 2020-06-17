def getLowestCommonAncestor(origin, a, b):
    a_depth = getDepth(a, origin)
    b_depth = getDepth(b, origin)

    #bring them to same level
    while a_depth != b_depth:
        if a_depth > b_depth:
            a = a.ancestor
            a -= 1
        else:
            b = b.ancestor
            b -= 1
    #find lowest common ancestor
    while a != b:
        a = a.ancestor
        b = b.ancestor
    return a

def getDepth(node, origin):
    depth = 0
    while node != origin:
        node = node.ancestor
        depth += 1
    return depth