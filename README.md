# Algorithmic-Desing-and-Techniques - edx Micromasters
Algorithmic Desing and Techniques - Study Material and Programming Assignment Repositories.

## Solving a Programming Challenge in Five Easy Steps:
  1. Reading Problem Statement
  2. Designing an Algorithm
  3. Implementing an Algorithm
  4. Testing and Debugging
  5. Submitting to the Grading System

## Why does a problem has constraints and what do they signify?:

The constraints whatever they be, provide the base for any coder to write a programme.ie… whether the algorithm which you are following to solve a problem is suitable for the given constraints or not .

Let me explain this with the help of a few examples:

Suppose for the below constraints we have to solve a problem , say sort a list of given no’s:
  1<=N<=1000
>So here even if you use an **O(n^2)** algorithm for sorting say bubble sort , it would work without an problem . The reason being that a computing machine can do upto 10^6/10^7 computations per second.

But if the constraint is,
  1< =N<=100000
>Now to sort a list with 100000 elements ie… 10^10 computations need to be done for the above n^2 algorithm would obviously time out, thus we use qsort/mergesort **O(nlogn)**.

Now suppose a problem has very high constraints say:
  1<=N<=10^18
>So in such a case your mind should come up with solutions with **O(logn)** complexity, because even O(n) would time out for the reasons mentioned above .

Some Extra things to be kept in mind:
* Suppose in a problem , if you think that solution for a problem is O(n^2) / any other polynomial complexity , then here Dynamic programming can help you to optimise the solution .
* Crux of The discussion : So what we can conclude is that the constraints always help you to plan which data structure / algorithm is to be followed to solve a computing problem .

Some useful links :
* If in case you are not familiar with the big(0) notation , this link will help you get started:
  http://www.codenlearn.com/2011/07/understanding-algorithm-complexity.html 71
* In case of any doubt regarding learning new data structures / dp / anything , the below is the go to page:
  http://help.topcoder.com/data-science/competing-in-algorithm-challenges/algorithm-tutorials/ 33

REFERENCE: https://discuss.codechef.com/t/constraints-in-problems/6621/3