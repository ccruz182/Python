def main():
    days_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days_fr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # Iter.
    i_en = iter(days_en)
    print(next(i_en))
    print(next(i_en))

    # Function + Sentinel.
    with open("built-in/testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # Enumerate reduces code w/counter.
    for i, m in enumerate(days_en, start=1):
        print(i, m)

    # Zip.
    for i, m in enumerate(zip(days_en, days_fr), start=1):
        print(i, m[0], "=", m[1], "in French")


if __name__ == "__main__":
    main()