def printPaths(data, stack=[], output=[]):
    for k in data.keys():
        v = data[k]
        stack.append(k)
        if v is None:
            output.append(".".join(stack))
        elif type(v) == list:
            for i,e in enumerate(v):
                if e is None:
                    s = ".".join(stack)+"."+str(i)
                    output.append(s)
        elif type(v) == dict:
            printPaths(v, stack, output)
        stack.pop()
    return output

a = {
    "Jon": "Smith",
    "Adam": ["Jake", None, "Nancy"],
    "Alex": {
        "Muller": [None, "Sam"],
        "Phil": None,
        "Xav": ["Mike", "Tom"]
    },
    "Lex": None,
}

print(printPaths(a))
op = []
def bt(ip, path):
    if not ip:
        op.append(path)
    elif type(ip) == list:
        for i in range(len(ip)):
            bt(ip[i], path + "." +str(i))
    elif type(ip) == dict:
        for i in ip:
            bt(ip[i], path + str(["." if path else ""][0]) + str(i))

bt(a, "")
print(op)

def random(a):
    c = {}
    for i in range(4):
        for j in range(4):
            a[i],a[j] = a[j], a[i]


