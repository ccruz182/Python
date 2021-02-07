class Person():
    def __init__(self):
        self.first_name = "Cesar"
        self.last_name = "Cruz"
        self.age = 23
    
    def __repr__(self):
        return "<Person Class - first_name:{0}, , last_name:{1}, age:{2}>".format(self.first_name, self.last_name, self.age)

    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.first_name, self.last_name, self.age)
    
    def __bytes__(self):
        val = "Person {0}:{1}:{2}".format(self.first_name, self.last_name, self.age)
        return bytes(val.encode('utf-8'))

def main():
    person1 = Person()
    print(repr(person1))
    print(str(person1))
    print("Formated: {0}".format(person1))
    print(bytes(person1))



if __name__ == "__main__":
    main()