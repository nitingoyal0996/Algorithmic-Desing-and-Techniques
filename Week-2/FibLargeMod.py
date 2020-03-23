'''
Problem Description
    Task. Given two integers n and m, output F n mod m (that is, the remainder of F n when divided by m).
    Input Format. The input consists of two integers n and m given on the same line (separated by a space).
    Constraints. 1 ≤ n ≤ 10^18 , 2 ≤ m ≤ 10^5 .
    Output Format. Output F n mod m.
'''

# Approach-I: Naive
'''
def FibModNaive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
'''

# Approach-II: Tail Recursion - Memorization
'''
Function returns very large Fibonacci numbers at ease.
Max Recursion Default Depth: 999
Can't compute numbers beyond this.

Please note that higher order fibonacci will require 
higher recursion limit. Although this can be set as follows

    import sys
    sys.setrecursionlimit(1500)

but doing so is dangerous -- the standard limit is a little conservative, 
but Python stackframes can be quite big. Hence, note the best way as 
tail recursion is not a particularly efficient technique.

def calFib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = calFib(n-1, computed) + calFib(n-2, computed)
    return computed[n]
'''

# Approach-II: Fast - Pisano period
'''
Pisano period:
    For any integer m ≥ 2, the sequence F n mod m is periodic. 
    The period always starts with 01 and is known as Pisano period
'''
def FibModFast(n, m):
    # Given two integers n and m, output Fn mod m (that is, the remainder of Fn when divided by m
    # Initialize a matrix [[1,1],[1,0]]    
    v1, v2, v3 = 1, 1, 0
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2

# Deliver Method
if __name__ == '__main__':
    x = input()
    n, m = int(x.split()[0]),int(x.split()[1])
    print(FibModFast(n, m))