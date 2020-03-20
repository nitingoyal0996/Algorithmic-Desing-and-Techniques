import random

# Max time required in nested for was 10.01 sec.
# while Max time required in the later approach was only 0.16 sec.

def takeSysInput():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

'''
Approach - I: Nested for loops
Time Complexity:
'''
def MaxProdNaive(a):
    result = 0
    n = len(a)
    for i in range(0,n):
        for j in range(i+1,n):
            temp = a[i]*a[j]
            if temp > result:
                result=temp
    return result

'''
Approach - II: Sort first and multiply later - Swapping
Time Complexity:
'''
def MaxProdFast(a):
    result = 0
    n = len(a)
    first = 0
    second = 0
    for i in range(0, n):
        if(a[i]>first):
            second = first
            first = a[i]
        elif(a[i]>second):
            second = a[i]
    result = first*second
    return result

'''
Approach - III: finding the largest and second largest Numbers
Time Complexity:

MaxPairwiseProductFast(A[1 . . . n]):
index 1 ← 1
for i from 2 to n:
if A[i] > A[index 1 ]:
index 1 ← i
index 2 ← 1
for i from 2 to n:
if i != index 1 and A[i] > A[index 2 ]:
index 2 ← i
return A[index 1 ] · A[index 2 ]
'''

#Stress testing

def StressTest():
    a = []
    n = 20
    print(n)
    while(n>=0):
        for i in range (0, n):
            a.append(random.randint(0,10000))
        print('\n')
        x = MaxProdNaive(a)
        y = MaxProdFast(a)
        if(x!=y):
            print('Wrong Answer: ' + str(x) + ' ' + str(y) + '\n')
        else:
            print('OK\n')
        n = n-1

StressTest()