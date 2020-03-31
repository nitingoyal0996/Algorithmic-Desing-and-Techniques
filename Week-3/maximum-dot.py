"""
Problem Introduction:
    You have n ads to place on a popular Internet page. For each ad, you know how
    much is the advertiser willing to pay for one click on this ad. You have set up n
    slots on your page and estimated the expected number of clicks per day for each
    slot. Now, your goal is to distribute the ads among the slots to maximize the
    total revenue.

Problem Description:
Task:           Given two sequences a 1 , a 2 , . . . , a n (ai is the profit per click of the i-th ad) and b 1 , b 2 , . 
                . . , b n (bi is the average number of clicks per day of the i-th slot), we need to partition them into n 
                pairs (a i , b j )such that the sum of their products is maximized.
Input Format:   The first line contains an integer n, the second one contains a sequence of integers a1 , a2 , . . . , an , 
                the third one contains a sequence of integers b 1 , b 2 , . . . , b n.
                *Constraints*. 1 ≤ n ≤ 10^3 ; −10^5 ≤ ai , bi ≤ 10^5 for all 1 ≤ i ≤ n.
Output Format.  Output the maximum value of
                n
                ∑︀ b1, b2, . . . , bn .
                i=1
"""

def maxDotProduct(a, b):
    '''
    Approach-I: Put Ad maximum revenue on slot with maximum average number of clicks per day.
    '''
    #Sort a, decreasing
    a.sort(reverse=True)
    # Sort b, decreasing
    b.sort(reverse=True)
    res = 0    
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n = input()
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    print(maxDotProduct(a, b))