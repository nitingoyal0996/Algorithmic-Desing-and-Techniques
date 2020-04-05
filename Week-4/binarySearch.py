'''
Problem Introduction:
    In this problem, you will implement the binary search algorithm that allows searching
    very efficiently (even huge) lists, provided that the list is sorted.

Problem Description:

Task:           The goal in this code problem is to implement the binary search algorithm.
Input Format:   The first line of the input contains an integer n and a sequence a 0 < a 1 < . . . < a n−1
                of n pairwise distinct positive integers in increasing order. The next line contains an integer k and k
                positive integers b 0 , b 1 , . . . , b k−1 .
Constraints:    1 ≤ n, k ≤ 10 4 ; 1 ≤ a i ≤ 10 9 for all 0 ≤ i < n; 1 ≤ b j ≤ 10 9 for all 0 ≤ j < k;
Output Format:  For all i from 0 to k − 1, output an index 0 ≤ j ≤ n − 1 such that a j = b i or −1 if there
                is no such index
'''

# Iterative Binary Solution
'''
def binarySearch(a, key):
    a.sort()
    print(a)
    left, right = 0, len(a)
    # write your code here
    while(left<=right):
        # print(left,right)
        mid = left + (right-left)//2 # Need to check
        # print(mid)
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
'''
import math
def binarySearch(source_list, key, low=0, high=None):
    high = len(source_list)-1
    if high < low:
        return -1 # Not found

    mid = int(math.floor(low + ((high - low) / 2)))

    if key == source_list[mid]:
        return mid
    elif key < source_list[mid]:
        return binarySearch(source_list, key, low, mid - 1)
    else:
        return binarySearch(source_list, key, mid + 1, high)

'''
def binarySearch(arr, x): 
    l = 0
    r = len(arr)-1
    print (l, r)
    while l <= r: 
  
        mid = l + (r - l)//2 
        print(mid)
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1

# Linear Search - not gonna do it.
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


To improve or generalise it to unsorted array as input
this algorithm can be modified to map an unsorted array elements
to an array with pointers. and then solve the equation and then 
map the output with the stored map.
'''

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    n = a[0]
    k = b[0]  
    for x in b[1:]:
        # replace with the call to binary_search when implemented
        # print(str(x)+'-')
        print(binarySearch(a[1:], x), end = ' ')
