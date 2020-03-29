'''
Problem Introduction
    In this problem, you will design and implement an elementary greedy algorithm
    used by cashiers all over the world millions of times per day.

Problem Description
    Task. The goal in this problem is to find the minimum number of coins needed to change the input value
    (an integer) into coins with denominations 1, 5, and 10.
    Input Format. The input consists of a single integer m.
    Constraints. 1 ≤ m ≤ 10 3 .
    Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m.
'''

def getChange(amount):
    coins = [10, 5, 1]
    number = 0
    for coin in coins:
        # Iterating over remaining amount with smaller coin
        while(amount>=coin):
            number += amount // coin
            amount %= coin
            print(amount)
    return number

if __name__ == '__main__':
    m = int(input())
    print(getChange(m))
