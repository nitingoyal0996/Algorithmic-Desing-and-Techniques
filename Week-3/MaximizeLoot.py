'''
Problem Introduction
    A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
    of items assuming that any fraction of a loot item can be put into his bag.

Problem Description
    Task.           The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
    Input Format.   The first line of the input contains the number n of items and the capacity W of a knapsack.
                    The next n lines define the values and weights of the items. The i-th line contains integers v i and w i —the
                    value and the weight of i-th item, respectively.
                    Constraints. 1 ≤ n ≤ 10 3 , 0 ≤ W ≤ 2 · 10 6 ; 0 ≤ v i ≤ 2 · 10 6 , 0 < w i ≤ 2 · 10 6 for all 1 ≤ i ≤ n. All the
                    numbers are integers.
    Output Format.  Output the maximal value of fractions of items that fit into the knapsack.
'''
# using python3
# Approach-I: running time complexity: O(n^2)
'''
def BestItem(weights, values):
    # a --> weight array, b --> value array
    maxValuePerWeight = 0
    bestItem = 0
    n = len(weights)
    for i in range(0, n):
        if weights[i] > 0:
            if (values[i]/weights[i]) > maxValuePerWeight:
                maxValuePerWeight = (values[i]/weights[i])
                bestItem = i
    return i

def knapsack(W, weights, values):
    totalValue = 0
    n = len(weights)
    for i in range(0, n):
        if W == 0:
            return totalValue
        i = BestItem(weights, values)
        a = min(weights[i], W)
        print(totalValue, a, i)
        totalValue += a*(values[i]/weights[i])
        weights[i] -= a
        W -= a
    return totalValue
'''

# Approach-II: running time complexity: O(nlogn)
'''
First sort the items with decreaing value per unit weight
then choose which item to put into knapsack
'''

def knapsackFast(W, weights, values):
    # variable initialize
    totalValue = 0
    n = len(weights)
    # Sorting
    valuePerUnitWeight = [(y,x,float(y/x)) for x,y in zip(w,v)]
    valuePerUnitWeight.sort(key= lambda tup: tup[2],reverse=True)
    # Rearrangement
    values = [x for tup in valuePerUnitWeight for x in values if tup[0]==x]
    weights = [y for tup in valuePerUnitWeight for y in weights if tup[1]==y]
    # iterate and select item from sorted list
    for i in range(0, n):
        if W == 0:
            return totalValue
        a = min(weights[i], W)
        totalValue += a*(float(values[i]/weights[i]))
        weights[i] -= a
        W -= a
    return totalValue


if __name__ == '__main__':
    (n, W) =  map(int, input().split())
    w = []
    v = []
    while n>0:
        (x,y) = map(int, input().split())
        v.append(x) # weight
        w.append(y) # value
        n -= 1
    # print(knapsack(W, w, v))
    print(knapsackFast(W,w,v))