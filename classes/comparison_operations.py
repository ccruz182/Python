class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "<Point x={0}, y={1}>".format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __ge__(self, other):
        return (pow(self.x, 2) + pow(self.y, 2)) >= (pow(other.x, 2) + pow(other.y, 2))
    
    def __gt__(self, other):
        return (pow(self.x, 2) + pow(self.y, 2)) > (pow(other.x, 2) + pow(other.y, 2))

    def __le__(self, other):
        return (pow(self.x, 2) + pow(self.y, 2)) <= (pow(other.x, 2) + pow(other.y, 2))
    
    def __lt__(self, other):
        return (pow(self.x, 2) + pow(self.y, 2)) < (pow(other.x, 2) + pow(other.y, 2))


def main():
    p1 = Point(10, 20)
    p2 = Point(-2, 5)
    p3 = Point(2, -5)

    print(p1 >= p2)
    print(p2 > p3)
    print(p2 < p3)
    print(p2 <= p3)
    

    
if __name__ == "__main__":
    main()
