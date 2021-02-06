from collections import Counter

def main():
    c1 = ["Bob", "Cesar", "Patrick", "Teresa"]
    c2 = ["Kimball", "Wayne", "Red John", "Teresa", "Bob"]

    counter1 = Counter(c1)
    counter2 = Counter(c2)

    # Values
    print(counter1["Patrick"])
    print(sum(counter1.values()), " in class")

    # Combining
    counter1.update(c2)
    print(sum(counter1.values()), " in class")

    # Most common
    print(counter1.most_common(3))

    # Separate
    counter1.subtract(c2)
    print(sum(counter1.values()), " in class")

    # Common between
    print(counter1 & counter2)




if __name__ == "__main__":
    main()
    