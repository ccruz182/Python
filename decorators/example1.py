def my_decorator(funct):
    def wrapper():
        a = funct()
        return a
    
    return wrapper

@my_decorator
def print_fibo():
    return 'Fibonacci'

pfib = my_decorator(print_fibo)
print(pfib())
print(print_fibo())