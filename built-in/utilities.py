def main():
    # Any & all
    list1 = [0, 1, 2, 3, 4, -304, 30]
    print("Any:", any(list1))
    print("All:", all(list1))

    # Max & min
    print("Max:", max(list1))
    print("Min:", min(list1))

    # Sum
    print("Sum:", sum(list1))


if __name__ == "__main__":
    main()