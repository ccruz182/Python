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


def main():
    p1 = Point(10, 20)
    p2 = Point(-2, 5)

    p3 = p1 + p2
    p4 = p1 - p2
    print(p3)
    print(p4)
    

    
if __name__ == "__main__":
    main()
