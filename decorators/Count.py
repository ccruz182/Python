from functools import lru_cache

class Count:
    def __init__(self, func):
        self.func = func
        self.cnt = 0
    
    def __call__(self, *args, **kwargs):
        self.cnt += 1
        print("Current count {0}".format(self.cnt))
        result = self.func(*args, **kwargs)
        return result

@lru_cache(maxsize=None)
@Count
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(4))