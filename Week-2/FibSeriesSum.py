'''
Problem Introduction
    The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers.

Problem Description
    Task. Given an integer n, find the last digit of the sum F 0 + F 1 + · · · + F n .
    Input Format. The input consists of a single integer n.
    Constraints. 0 ≤ n ≤ 10 14 .
    Output Format. Output the last digit of F 0 + F 1 + · · · + F n .
'''

# Approach-II - Fast Relationship based
'''
Last Digit of the Sum of Fibonacci Numbers
Given the following relationship between sequences exist:

    0 1 1 2 3 5 8 13 21 34      // fibs
          1 2 4 7 12 20 33      // sums

We need to compute the last digit of F(n+2) --- using Pisano Period --- and substract 1
'''
'''
int fibonacci_sum_fast(long long n) {
    std::vector<int> p{0, 1, 1 % 10};  // Pisano period

    for (int i = 2; true; ++i) {
        int current = (p[i] + p[i - 1]) % 10;
        if (p[i] == 0 && current == 1) {
            p.pop_back();
            break;
        }
        p.push_back(current);
    }

    int fib = p[(n + 2) % p.size()];  // F(n+2) % 10
    // Handle decrementing 0 by adding 9 and returning last digit.
    return (fib + 9) % 10;
}

def Fib(n):
    p = [0,1,1%10]
    for i in range(2, ):
        current = (p[i]+p[i-1]) % 10
        if (p[i] == 0 and current == 1):
            p.pop()
            break
        p.append()
    fib = p[(n+2) % len(p)]
    print(fib+9)
    return (fib + 9) % 10
'''
def FibSeriesSumLastD(n, m):  
    v1, v2, v3 = 1, 1, 0
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n+2)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2-1

# Deliver Method
if __name__ == '__main__':
    x = input()
    n, m = int(x.split()[0]),int(x.split()[1])
    print(FibSeriesSumLastD(n,m))