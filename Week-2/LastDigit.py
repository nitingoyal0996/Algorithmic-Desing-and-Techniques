'''
Problem Goal:
Goal in this problem is to find the last digit of n-th Fibonacci number.
'''

# Uses python3

# Approach - I: Naive Method
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
 
    return current % 10

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
    print("LastDigit is being called directly")
else:
    print("LastDigit is not being called directly")