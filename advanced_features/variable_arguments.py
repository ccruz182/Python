
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result



def main():
    print(addition(1,2, 10))
    my_nums = [1, 2, 3, 4]
    print(addition(*my_nums))


if __name__ == "__main__":
    main()