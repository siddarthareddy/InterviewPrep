def is_balanced_1(input_str):
    close_for_open = { '(': ')', '[': ']', '{': '}' }

    stack = []
    for c in input_str:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if len(stack) == 0:
                return False

            o = stack.pop()
            if close_for_open[o] != c:
                return False

    return len(stack) == 0


# function to check if parenthesis
# are balanced.
def check(expr, n):
    pairs = {'(':')', '{':'}', '[':']'}
    # Base cases
    if n == 0:
        return True
    if n == 1:
        return False
    if expr[0] in pairs.values():
        return False

    # Search for closing bracket for first
    # opening bracket.
    closing = pairs[expr[0]]

    # count is used to handle cases like
    # "((()))". We basically need to
    # consider matching closing bracket.
    i = -1
    count = 0
    for i in range(1, n):
        if expr[i] == expr[0]:
            count += 1
        if expr[i] == closing:
            if count == 0:
                break
            count -= 1

    # If we did not find a closing
    # bracket
    if i == n:
        return False

    # If closing bracket was next
    # to open
    if i == 1:
        return check(expr[2:], n - 2)

    # If closing bracket was somewhere
    # in middle.
    return check(expr[1:], i - 1) and check(expr[i + 1:], n - i - 1)


def isBalanced(expr):
    n = len(expr)

    if check(expr, n):
        print(expr, " is Balanced")
    else:
        print(expr, " is Not Balanced")

def is_balanced_2(input_str, close_for_open, stack=[]):

    if len(input_str) == 0:
        return len(stack) == 0

    c = input_str[0]
    rest = input_str[1:]

# continuation of - def is_balanced_2
    is_balanced_as_open = False
    if c in close_for_open.keys():  # possible open delimiter
        stack.append(c)
        is_balanced_as_open = is_balanced_2(rest, close_for_open, stack)
        stack.pop()
    if is_balanced_as_open:
        return is_balanced_as_open

# continuation of - def is_balanced_2
    is_balanced_as_close = False
    if c in close_for_open.values(): # possible close delimiter
        if len(stack) > 0:
            o = stack.pop()
            if close_for_open[o] == c:
                is_balanced_as_close = is_balanced_2(rest, close_for_open, stack)

            stack.append(o)
# continuation of - def is_balanced_2
    return is_balanced_as_close


# # Driver Code
# if __name__ == "__main__":
#     expr = "[(])"
#     isBalanced(expr)
#     isBalanced("(([{}]))")
#     isBalanced("(([{]}))")
close_for_open= {'a':'A', 'A':'b'}
print(close_for_open)
print(is_balanced_2('aAbA', close_for_open))
print(is_balanced_2('aAAb', close_for_open))
print(is_balanced_2('abAb', close_for_open))

# def is_balanced_2(input_str):
#     close_for_open = { '(': ')', '[': ']', '{': '}' }
#
#     c = input_str[0]
#     if c in '({[':
#         is_balanced_2(input_str[1:])
#         elif c in ')}]':
#             if len(stack) == 0:
#                 return False
#
#             o = stack.pop()
#             if close_for_open[o] != c:
#                 return False
#
#     return len(stack) == 0

# print(is_balanced_1("(([{}]))"))
# print(is_balanced_1("(([{]}))"))