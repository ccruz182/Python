
def my_function_1(arg1, arg2=None):
    """ my_function_1(arg1, arg2=None) -> Doesn't really do anything

    Parameters:
        * arg1: First argument.
        * arg2: Second argument. Optional
    """
    print(arg1, arg2)

def main():
    print(my_function_1.__doc__)


if __name__ == "__main__":
    main()