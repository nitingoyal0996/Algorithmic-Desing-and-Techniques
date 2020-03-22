'''
Problem Goal:
    Goal in this problem is to find the last digit of n-th Fibonacci number.

Problem Description:
    Task. Given an integer n, find the last digit of the nth Fibonacci number F n (that is, F n mod 10).
    Input Format. The input consists of a single integer n.
    Constraints. 0 ≤ n ≤ 10^7 .
    Output Format. Output the last digit of F n .
'''

# Approach-I: Naive Method
'''
def LastDigitNaive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
 
    return current % 10
'''

# Approach-II: Fast Method
def LastDigitFast(n):
    if n<0: print("Please enter a value greater than 0")
    elif n>=0 and n<=1: return n
    else:
        a, b, c = 1, 1, 0
        for i in range(3, n+1):
            c = b
            b = a
            a = (b + c) % 10
        return a        

# Deliver Method
if __name__ == '__main__':
    n = int(input())
    # print(LastDigitNaive(n))
    print(LastDigitFast(n))
    # print("LastDigit is being called directly")
# else:
    # print("LastDigit is not being called directly")