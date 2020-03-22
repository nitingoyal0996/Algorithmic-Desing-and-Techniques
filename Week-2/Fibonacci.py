'''
Problem-1 Description:
    Task: Given an integer n, find the nth Fibonacci number Fn .
    Input Format: The input consists of a single integer n.
    Constraints: 0 ≤ n ≤ 45.
    Output Format: Output Fn
'''
import random
import sys

# Approach-I: Naive
'''
def FibNaive(n): 
	if n<0: 
		print("Incorrect input") 
	# First Fibonacci number is 0 
	elif n==0: 
		return 0
	# Second Fibonacci number is 1 
	elif n==1: 
		return 1
	else: 
		return FibNaive(n-1)+FibNaive(n-2) 
'''

# Approach-II: Fast
def FibFast(n):
    if(n<0):
        print("please enter a number greater than 0.")
    elif(n==1 or n==0):
        return n
    else:
        a, b, c = 1, 0, 1
        for i in range (2, n+1):
            a = b + c
            b = c
            c = a
            # print(a)
        return a

# Deliver Method
n = int(input())
print(FibFast(n))
# print(FibNaive(n))

# Stress Test
'''
def StressTest():
    a = []
    n = random.randint(0,12)
    print(n)
    while(n>=0):
        a = (random.randint(0,10000))
        print('\n')
        x = FibFast(n)
        y = FibNaive(n)
        if(x!=y):
            print('Wrong Answer: ' + str(x) + ' ' + str(y) + '\n')
        else:
            print('OK\n')
        n = n-1

StressTest()    
'''