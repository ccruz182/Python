from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    WATERMELON = 4
    PEAR = auto()

def main():
    print(Fruit.APPLE)

    print(Fruit.PEAR.name, Fruit.PEAR.value)



if __name__ == "__main__":
    main()