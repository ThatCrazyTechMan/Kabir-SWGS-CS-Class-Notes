def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibSequence(end):
    for i in range(0, end):
        print(fib(i))

fibSequence(20)