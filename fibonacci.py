def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    for n in range(5, 10):
        print 'fib({0}) = {1}'.format(n, fib(n))
