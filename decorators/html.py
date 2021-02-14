def bold(func):
    def wrapper():
        result = func()
        return "<b>{0}</b>".format(result)
    
    return wrapper

def italic(func):
    def wrapper():
        result = func()
        return "<i>{0}</i>".format(result)
    
    return wrapper

@bold
@italic
def print_fibo():
    return 'Fibonacci'

print(print_fibo())