### Problem Statement:

Maximum Pairwise Product Problem
Find the maximum product of two distinct numbers
in a sequence of non-negative integers.

Input: 
A sequence of non-negative
integers.

Output: 
The maximum value that
can be obtained by multiplying
two different elements from the sequence


### Stress Test:
A stress test consists of four parts:
1. Your implementation of an algorithm.
2. An alternative, trivial and slow, but correct implementation of an
algorithm for the same problem.
3. A random test generator.
4. An infinite loop in which a new test is generated and fed into both
implementations to compare the results. If their results differ, the
test and both answers are output, and the program stops, otherwise
the loop repeats.


### Deterministic Programs vs Non-Deterministic programs:
Note that our solutions worked and then failed on exactly the same
test cases as on the previous run of the stress test, because we didn’t
change anything in the test generator. The numbers it uses to generate
tests are pseudorandom rather than random—it means that the sequence
looks random, but it is the same each time we run this program. It is
a convenient and important property, and you should try to have your
programs exhibit such behavior, because deterministic programs (that al-
ways give the same result for the same input) are easier to debug than
non-deterministic ones.


### Exercise Break Question:
For now I'm mentioning these questions here. I'll put the solutions very soon.

1. Find two largest elements in an array in 1.5n comparisons.
2. Find two largest elements in an array in n + [log 2 n] − 2 comparisons.

if you think previous exercise was easy, here are next two challenges that you may face:

3. Prove that no algorithm for finding two largest elements in an array can do this in less than n + [log 2 n] − 2 comparisons.
4. What is the fastest algorithm for finding three largest elements?

### More Compact Algorithm
The Maximum Pairwise Product Problem can be solved by the following
compact algorithm that uses sorting (in non-decreasing order).

    MaxPairwiseProductBySorting(A[1 . . . n]):
    Sort(A)
    return A[n − 1] · A[n]

This algorithm does more than we actually need: 
    instead of finding two
largest elements, it sorts the entire array. For this reason, its running time
is O(n log n), but not O(n). Still, for the given constraints (2 ≤ n ≤ 2 · 10 5 )
this is usually sufficiently fast to fit into a second and pass our grader.