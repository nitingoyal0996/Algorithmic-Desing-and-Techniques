### Methods:
1. Naive Nested Loops  - 0(n*2)
2. Binary Search Tree  - 0(nlogn)
3. Moore's Voting Algorithm - 0(n)
4. Hashmaps - 0(n)
5. Sorting - 0(nlogn)
6. Divide & Conqure - 0(nlogn)


### Majority Element
Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element". A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).
Examples :
    Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
    Output : 4
    Explanation: The frequency of 4 is 5 which is greater
    than the half of the size of the array size. 

    Input : {3, 3, 4, 2, 4, 4, 2, 4}
    Output : No Majority Element
    Explanation: There is no element whose frequency is
    greater than the half of the size of the array size.
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.



 
## METHOD 1

#### Approach: 
The basic solution is to have two loops and keep track of the maximum count for all different elements. If maximum count becomes greater than n/2 then break the loops and return the element having maximum count. If the maximum count doesn’t become more than n/2 then majority element doesn’t exist.

#### Algorithm:
* Create a variable to store the max count, count = 0
* Traverse through the array from start to end.
* For every element in the array run another loop to find the count of similar elements in the given array.
* If the count is greater than the max count update the max count and store the index in another varaible.
* If the maximum count is greater than the half the size of the array, print the element. Else print there is no majority element.

#### Implementation:

# Python 3 program to find Majority  
# element in an array 

    def findMajority(arr, n): 
    
        maxCount = 0; 
        index = -1 # sentinels 
        for i in range(n): 
        
            count = 0
            for j in range(n): 
            
                if(arr[i] == arr[j]): 
                    count += 1
            
            # update maxCount if count of  
            # current element is greater 
            if(count > maxCount): 
            
                maxCount = count 
                index = i 
        
        # if maxCount is greater than n/2  
        # return the corresponding element  
        if (maxCount > n//2): 
            print(arr[index]) 
        
        else: 
            print("No Majority Element") 
    
    # Driver code 
    if __name__ == "__main__": 
        arr = [1, 1, 2, 1, 3, 5, 1] 
        n = len(arr) 
        
        # Function calling  
        findMajority(arr, n) 

Output:
1

#### Compelxity Analysis:
    Time Complexity: O(n*n).
    A nested loop is needed where both the loops traverse the array from start to end, so the time complexity is O(n^2).
    Auxiliary Space : O(1).
    As no extra space is required for any operation so the space complexity is constant.
 
## METHOD 2 (Using Binary Search Tree)

#### Approach: 
Insert elements in BST one by one and if an element is already present then increment the count of the node. At any stage, if the count of a node becomes more than n/2 then return.

#### Algorithm:
*   Create a binary search tree, if same element is entered in the binary search tree the frequency of the node is increased.
*   traverse the array and insert the element in the binary search tree.
*   If the maximum frequency of any node is greater than the half the size of the array, then perform a inorder traversal and find the node with frequency greater than half
*   Else print No majority Element.

#### Implementation:
    // C++ program to demonstrate insert operation in binary search tree.  
    #include<bits/stdc++.h>   
    using namespace std; 
    
    struct node  
    {  
        int key; 
        int c = 0; 
        struct node *left, *right;  
    };  
    
    // A utility function to create a new BST node  
    struct node *newNode(int item)  
    {  
        struct node *temp = (struct node *)malloc(sizeof(struct node));  
        temp->key = item; 
        temp->c = 1; 
        temp->left = temp->right = NULL;  
        return temp;  
    }  
    
    
    /* A utility function to insert a new node with given key in BST */
    struct node* insert(struct node* node, int key,int &ma)  
    {  
        /* If the tree is empty, return a new node */
        if (node == NULL)  
        { 
            if(ma==0) 
                ma=1; 
            
            return newNode(key);  
        } 
        
        /* Otherwise, recur down the tree */
        if (key < node->key)  
            node->left = insert(node->left, key, ma);  
        else if (key > node->key)  
            node->right = insert(node->right, key, ma);  
        else
            node->c++; 
            
        //find the max count 
        ma = max(ma, node->c); 
        
        /* return the (unchanged) node pointer */
        return node;  
    }  
    // A utility function to do inorder traversal of BST  
    void inorder(struct node *root,int s)  
    {  
        if (root != NULL)  
        {  
            inorder(root->left,s); 
            
            if(root->c>(s/2)) 
                printf("%d \n", root->key);  
            
            inorder(root->right,s);  
        }  
    }  
    
    // Driver Program to test above functions  
    int main()  
    {  
        int a[] = {1, 3, 3, 3, 2}; 
        int size = (sizeof(a))/sizeof(a[0]); 
        
        struct node *root = NULL;  
        int ma=0; 
        
        for(int i=0;i<size;i++) 
        { 
            root = insert(root, a[i],ma);  
        } 
        
        if(ma>(size/2)) 
            inorder(root,size); 
        else 
            cout<<"No majority element\n"; 
        return 0;  
    }  

Output: 3

#### Compelxity Analysis:
    Time Complexity : If a Binary Search Tree is used then time complexity will be O(n^2). If a self-balancing-binary-search tree is used then it will be O(nlogn)
    Auxiliary Space : O(n).
    As extra space is needed to store the array in tree.
 

## METHOD 3 (Using Moore’s Voting Algorithm): 

This method only works when the majority element does exist in the array. In the problem definition, it is said that the majority element may or may not exist but for applying this approach let’s assume that the majority element does exist in the given input array.

#### Approach: This is a two-step process.
1. The first step gives the element that maybe the majority element in the array. If there is a majority element in an array, then this step will definitely return majority element, otherwise, it will return candidate for majority element.
2. Check if the element obtained from the above step is majority element. This step is necessary as there might be no majority element.

##### Step 1: Finding a Candidate
The algorithm for the first phase that works in O(n) is known as Moore’s Voting Algorithm. Basic idea of the algorithm is that if each occurrence of an element e can be cancelled with all the other elements that are different from e then e will exist till end if it is a majority element.

##### Step 2: Check if the element obtained in step 1 is majority element or not.
Traverse through the array and check if the count of the element found is greater than half the size of the array, then print the answer else print “No majority element”.

#### Algorithm:
* Loop through each element and maintains a count of majority element, and a majority index, maj_index
* If the next element is same then increment the count if the next element is not same then decrement the count.
* if the count reaches 0 then changes the maj_index to the current element and set the count again to 1.
* Now again traverse through the array and find the count of majority element found.
* If the count is greater than half the size of the array, print the element
* Else print that there is no majority element

#### Implementation:

    def findCandidate(A): 
        maj_index = 0
        count = 1
        for i in range(len(A)): 
            if A[maj_index] == A[i]: 
                count += 1
            else: 
                count -= 1
            if count == 0: 
                maj_index = i 
                count = 1
        return A[maj_index] 
    
    # Function to check if the candidate occurs more than n/2 times 
    def isMajority(A, cand): 
        count = 0
        for i in range(len(A)): 
            if A[i] == cand: 
                count += 1
        if count > len(A)/2: 
            return True
        else: 
            return False
    
    # Function to print Majority Element 
    def printMajority(A): 
        # Find the candidate for Majority 
        cand = findCandidate(A) 
        
        # Print the candidate if it is Majority 
        if isMajority(A, cand) == True: 
            print(cand) 
        else: 
            print("No Majority Element") 
    
    # Driver program to test above functions 
    A = [1, 3, 3, 1, 2] 
    printMajority(A)  

Output:
No Majority Element 

#### Complexity Analysis:

    Time Complexity: O(n).
    As two traversal of the array is needed, so the time complexity is linear.
    Auxiliary Space : O(1).
    As no extra space is required.
 
## METHOD 4 (Using Hashmap):

#### Approach: 
This method is somewhat similar to Moore voting algorithm in terms of time complexity, but in this case, there is no need for the second step of Moore voting algorithm. But as usual, here space complexity becomes O(n).
In Hashmap(key-value pair), at value, maintain a count for each element(key) and whenever the count is greater than half of the array length, return that key(majority element).

#### Algorithm:
* Create a hashmap to store a key-value pair, i.e. element-frequency pair.
* Traverse the array from start to end.
* For every element in the array, insert the element in the hashmap if the element does not exist as key, else fetch the value of the key ( array[i] ) and increase the value by 1
* If the count is greater than half then print the majority element and break.
* If no majority element is found print “No Majority element”

#### Implementation:
    # Python program for finding out majority  
    # element in an array  
    
    def findMajority(arr, size): 
        m = {} 
        for i in range(size): 
            if arr[i] in m: 
                m[arr[i]] += 1
            else: 
                m[arr[i]] = 1
        count = 0
        for key in m: 
            if m[key] > size / 2: 
                count = 1
                print("Majority found :-",key) 
                break
        if(count == 0): 
            print("No Majority element") 
    
    # Driver code  
    arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]  
    n = len(arr) 
    
    # Function calling  
    findMajority(arr, n) 
    
    # This code is contributed by ankush_953 
    Output:

    Majority found :- 2

#### Complexity Analysis:
    Time Complexity: O(n).
    One traversal of the array is needed, so the time complexity is linear.
    Auxiliary Space : O(n).
    Since a hashmap requires linear space.

## METHOD 5: Sorting

#### Approach:
The idea is to sort the array. Sorting makes similar elements in the array adjacent, so traverse the array and update the count until the present element is similar to the previous one. If the frequency is more than half the size of the array, print the majority element.

#### Algorithm:
* Sort the array and create a varibale count and previous ,prev = INT_MIN.
* Traverse the element from start to end.
* If the current element is equal to the previous element increase the count.
* Else set the count to 1.
* If the count is greater than half the size of array, print the element as majority element and break.
* If no majority element found, print “No majority element”

#### Implementation:
    // C++ program to find Majority  
    // element in an array 
    #include <bits/stdc++.h> 
    using namespace std; 
    
    // Function to find Majority element 
    // in an array 
    // it returns -1 if there is no majority element 
    
    int majorityElement(int *arr, int n) 
    { 
        // sort the array in O(nlogn) 
        sort(arr, arr+n); 
        
        int count = 1, max_ele = -1, temp = arr[0], ele, f=0; 
        
        for(int i=1;i<n;i++) 
        { 
            // increases the count if the same element occurs 
            // otherwise starts counting new element 
            if(temp==arr[i]) 
            { 
                count++; 
            } 
            else
            { 
                count = 1; 
                temp = arr[i]; 
            } 
            
            // sets maximum count 
            // and stores maximum occured element so far 
            // if maximum count becomes greater than n/2 
            // it breaks out setting the flag 
            if(max_ele<count) 
            { 
                max_ele = count; 
                ele = arr[i]; 
                
                if(max_ele>(n/2)) 
                { 
                    f = 1; 
                    break; 
                } 
            } 
        } 
        
        // returns maximum occured element 
        // if there is no such element, returns -1 
        return (f==1 ? ele : -1); 
    } 
    
    
    // Driver code 
    int main() 
    { 
        int arr[] = {1, 1, 2, 1, 3, 5, 1}; 
        int n = sizeof(arr) / sizeof(arr[0]); 
        
        // Function calling  
        cout<<majorityElement(arr, n); 
    
        return 0; 
    } 
    Output:

    1

#### Complexity Analysis:
    Time Complexity : O(nlogn).
    Sorting requires O(n log n) time complexity.
    Auxiliary Space : O(1).
    As no extra space is required.

REF: https://www.geeksforgeeks.org/majority-element/

## Method 6: Divide and Conquer

#### Intuition
If we know the majority element in the left and right halves of an array, we can determine which is the global majority element in linear time.

#### Algorithm
Here, we apply a classical divide & conquer approach that recurses on the left and right halves of an array until an answer can be trivially achieved for a length-1 array. Note that because actually passing copies of subarrays costs time and space, we instead pass lo and hi indices that describe the relevant slice of the overall array. In this case, the majority element for a length-1 slice is trivially its only element, so the recursion stops there. If the current slice is longer than length-1, we must combine the answers for the slice's left and right halves. If they agree on the majority element, then the majority element for the overall slice is obviously the same1. If they disagree, only one of them can be "right", so we need to count the occurrences of the left and right majority elements to determine which subslice's answer is globally correct. The overall answer for the array is thus the majority element between indices 0 and nn.

#### Impelementation

    class Solution:
        def majorityElement(self, nums, lo=0, hi=None):
            def majority_element_rec(lo, hi):
                # base case; the only element in an array of size 1 is the majority
                # element.
                if lo == hi:
                    return nums[lo]

                # recurse on left and right halves of this slice.
                mid = (hi-lo)//2 + lo
                left = majority_element_rec(lo, mid)
                right = majority_element_rec(mid+1, hi)

                # if the two halves agree on the majority element, return it.
                if left == right:
                    return left

                # otherwise, count each element and return the "winner".
                left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
                right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

                return left if left_count > right_count else right

            return majority_element_rec(0, len(nums)-1)

#### Complexity Analysis

    Time complexity : O(nlgn)O(nlgn)

    Each recursive call to majority_element_rec performs two recursive calls on subslices of size n/2 and two linear scans of length nn. Therefore, the time complexity of the divide & conquer approach can be represented by the following recurrence relation:

        T(n) = 2T(n/2) + 2n
        T(n)=2T(2n)+2n

    By the master theorem, the recurrence satisfies case 2, so the complexity can be analyzed as such:

            T(n) = Θ(n^(logb-a)logn) = Θ(n^(log2-2)logn)
            T(n) = Θ(nlogn)​

REF: https://leetcode.com/articles/majority-element/