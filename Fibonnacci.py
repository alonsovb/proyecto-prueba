def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    fibonacci = fib(10)
    print('Fibonacci de orden 10:')
    print(fibonacci)
main()
