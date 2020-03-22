'''
Problem Description:
    Task. Given two integers a and b, find their greatest common divisor.
    Input Format. The two integers a, b are given in the same line separated by space.
    Constraints. 1 ≤ a, b ≤ 2 · 10^9 .
    Output Format. Output GCD(a, b).
'''

# Approach-I: Naive: checking every combination
'''
def gcdNaive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
'''

# Approach-II: Fast: Euclidean Algorithm
'''
Ref: https://en.wikipedia.org/wiki/Euclidean_algorithm

Key Lemma: gcd(a, b) = gcd(a′, b) = gcd(b, a′) 
Here,
    a, b: input integers
    a': remainder

Euclidean Algorithm:

    Function EuclidGCD(a, b)
        if b = 0:
            return a
        a′ ← the remainder when a is divided by b
            return EuclidGCD(b, a′)

Produces correct result by Lemma.
'''
def gcdFast(a, b):
    if b==0:
        return a
    else:
        return gcdFast(b, a%b)

if __name__ == "__main__":
    n = input()
    a = int(n.split()[0])
    b = int(n.split()[1])
    print(gcdFast(a, b))