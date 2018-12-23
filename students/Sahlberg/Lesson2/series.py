def fibonacci(n):
    """Returns the nth value of a Fibonacci series"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)