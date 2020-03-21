# Naive Approach
'''
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
'''
def FibFast(n):
    if(n<=1):
        return n
    
    else:
        c=0
        b=1
        a=1
        for i in range(3, n):
            c = i      # F(i-2) = F(i-1)
            print(a)
            b = a      # F(i-1) = F(i)
            print(a)
            a = b + c  # F(i) = F(-1) + F(-2)
    return a

n = int(input())
print(FibFast(n))