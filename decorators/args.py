from time import perf_counter

def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print("fib({0})={1} - Duration {2}".format(str(*args), result, duration))
        return result
    return wrapper

@timer
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(15)