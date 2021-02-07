from collections import deque

def main():
    d = deque("cesar")
    d.append("1")
    print(d)
    
    d.popleft()
    print(d)

    d.rotate(2)
    print(d)

if __name__ == "__main__":
    main()
    