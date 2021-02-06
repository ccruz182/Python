import itertools

def test_function(x):
    return x < 40




def main():
    # Cycle
    seq1 = ["Joe", "Carlos", "Corbin"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # Count
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # Accumulate
    vals = [10, 20, 30, 40, 30, 50]
    acc = itertools.accumulate(vals, max)
    print(list(acc))

    # Chain
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # Dropwhile and takewhile
    dw = itertools.dropwhile(test_function, vals)
    tw = itertools.takewhile(test_function, vals)
    print(list(dw))
    print(list(tw))




if __name__ == "__main__":
    main()