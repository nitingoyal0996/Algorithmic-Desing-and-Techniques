# Max time required in nested for was 10.01 sec. 
# while Max time required in the later approach was only 0.16 sec. 

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
result = 0

# Approach - I: Nested for loops - Not Good

# for i in range(0,n):
#     for j in range(i+1,n):
#         temp = a[i]*a[j]
#         if temp > result:
#             result=temp

# Approach - II: Sort first and multiply later

first = 0
second = 0
# finding max. pair
for i in range(0, n):
    if(a[i]>first):
        print(first, a[i])
        second = first
        first = a[i]
    elif(a[i]>second):
        print(second, a[i])
        second = a[i]
print(first)
print(second)
result = first*second
print(result)