
def celsius_to_fahrenheit(temp):
    return (temp * 9/5)+ 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def main():
    c_temps = [0, 28, 15]
    f_temps = [32, 90, 99]

    conv1 = map(celsius_to_fahrenheit, c_temps)
    conv2 = map(fahrenheit_to_celsius, f_temps)
    print(list(conv1))
    print(list(conv2))

    conv_l1 = map(lambda t: (t * 9/5)+ 32, c_temps)
    print(list(conv_l1))


if __name__ == "__main__":
    main()