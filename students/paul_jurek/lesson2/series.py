"""module to answer Fibonacci Series Exercise in Lesson 2"""


def fibonacci(n: int):
    """return nth value of fibonacci sequence starting with index 0
    args:
        n: non-negative integer for indicating sequence number to return

    returns:
        fib number at nth position
    """
    return sum_series(n=n,index0=0,index1=1)


def lucas(n: int):
    """return nth value of lucas sequence starting with index 0
    args:
        n: non-negative integer for indicating sequence number to return

    returns:
        lucas number at nth position
    """
    return sum_series(n=n,index0=2,index1=1)


def sum_series(n:int, index0:int=0, index1:int=1):
    """return nth index (starting at 0) of summing series.
    starting values defined by index0 and index1
    args:
        n: non-negative integer for indicating sequence number to return
        index0: number in first index of sereies
        index1: number in second index of series 
    returns:
        value at nth position in summing series"""
    
