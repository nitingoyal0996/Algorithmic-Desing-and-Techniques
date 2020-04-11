
'''
Recomputations of same subproblems can be avoided by constructing
a temporary array table[][] in bottom up manner. Below is Dynamic 
Programming based solution
'''
import sys
import math 


def minCoinsDp(money, coins):
    totalCoins = len(coins)
    
    # array to store min no of coins
    minCoins = [0 for i in range(money + 1)]
    # base case
    minCoins[0] = 0

    for m in range(1, money+1):
        minCoins[m] = sys.maxsize   # put initial value infinity
        # print('m: {0}'.format(m))
        for i in range(totalCoins):
            
            if coins[i] <= m:   # if m is greater than coin
                subResult = minCoins[m - coins[i]]
                # print('m - coins[i]: {0}'.format(m - coins[i]))
                # print('subResult: {0}'.format(subResult))

                # if subResult is neither infinity nor greater than minCoins[m]
                if (subResult != sys.maxsize and subResult+1 < minCoins[m]):
                    minCoins[m] = subResult + 1
    # print('minCoins: {0}'.format(minCoins))
    return minCoins[m]


if __name__ == '__main__':
    x = int(input())
    coins = [1, 3, 4]
    print(minCoinsDp(x, coins))