class Color():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100
    
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError
    
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)
    
    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")


def main():
    my_color = Color()
    print(my_color.rgbcolor)
    print(my_color.hexcolor)

    my_color.rgbcolor = (100, 200, 9)
    print(my_color.hexcolor)

    print(dir(my_color))
    
if __name__ == "__main__":
    main()
