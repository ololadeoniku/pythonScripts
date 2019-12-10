# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def fib_list(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    for i in range(n+1):
        result.append(a)
        a, b = b, a+b
    return result

print(fib(10))
print(fib_list(10))