import collections

def main():
    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape']

    fruits_counter = {}
    fruits_counter_dd = collections.defaultdict(int)

    for fruit in fruits:
        if fruit in fruits_counter.keys():
            fruits_counter[fruit] += 1  
        else:
            fruits_counter[fruit] = 1
        
        fruits_counter_dd[fruit] += 1


    print(fruits_counter)
    print(fruits_counter_dd)




if __name__ == "__main__":
    main()
    