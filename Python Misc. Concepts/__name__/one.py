# Module 1 Method: get fibonacci last digit Naive
def methodOne(n):    
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    n = int(input())
    print(methodOne(n))
    print("LastDigit is being called directly")
else:
    print("LastDigit is not being called directly")