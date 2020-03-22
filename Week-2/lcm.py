'''
Problem Description:
    Task. Given two integers a and b, find their least common multiple.
    Input Format. The two integers a and b are given in the same line separated by space.
    Constraints. 1 ≤ a, b ≤ 2 · 109 .
    Output Format. Output the least common multiple of a and b.
'''

# Approach-I: Naive - Checking all the combinations
'''
def lcm_naive(a, b):
    lcm = a*b
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            if l < lcm:
                lcm = l
    return lcm
'''

# Approach-II: Fast - Using GCD Formula
'''
If we know the greatest common divisor (GCD) of integers a and b, 
we can calculate the LCM using the following formula,

    LCM(a,b) = a*b / GCD(a,b)

'''
def gcdFast(a,b):
    if b==0:
        return a
    else:
        return gcdFast(b, a%b)

def lcmFast(a,b):
    prod = a*b
    gcd = gcdFast(a,b)
    lcm = prod // gcd
    return lcm

# Deliver Method
if __name__ == '__main__':
    n = input()
    a, b = int(n.split()[0]),int(n.split()[1])
    print(lcmFast(a, b))