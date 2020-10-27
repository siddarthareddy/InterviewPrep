def fib(n):
    a = 1
    b = 1
    for i in range(2,n):
        a, b = a+b, a
    print(a)
for i in range(1,10):
    fib(i)