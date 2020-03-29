'''
Aim: to rearrange lists on the basis of an already sorted list

Sorted list should contain a key element, so that rearrange can take place.
To achieve that tuple is being used.
'''
# Define lists
v = [8,5,6]
w = [1,10,3]

# Derived list
valuePerUnitWeight = [(y,x,y/x) for x,y in zip(w,v)]
print(valuePerUnitWeight)
# Output: [(8, 1, 8.0), (5, 10, 0.5), (6, 3, 2.0)]

# tuple sorting, On the basis of 3rd element in tuple  i.e. v per unit w.
# Order: Default, Increasing
valuePerUnitWeight.sort(key= lambda tup: tup[2])
print(valuePerUnitWeight)
# Output:[(5, 10, 0.5), (6, 3, 2.0), (8, 1, 8.0)]
# Order: Decreasing
valuePerUnitWeight.sort(key= lambda tup: tup[2],reverse=True)
print(valuePerUnitWeight)
# Output:[(8, 1, 8.0), (6, 3, 2.0), (5, 10, 0.5)]

# Rearranging v according to list valuePerUnitWeight
v = [x for tup in valuePerUnitWeight for x in v if tup[0]==x]
print(v)
# Output: [8, 6, 5]

# Rearranging w according to list valuePerUnitWeight
w = [y for tup in valuePerUnitWeight for y in w if tup[1]==y]
print(w)
# Output: [1, 3, 10]

# ----------------------------------------------------#
'''
Rearranging list b according to order of list za

There's actually a way to do this in linear O(n) time, because this isn't really a sorting
operation. The existence of the list b means that the sorting is already done; all we really 
need to do is to rearrange the elements of a to be in the same order. This can be done 
efficiently thanks to dictionaries.
'''

'''
from collections import defaultdict

def sorted_by(seq_to_sort, desired_order, key=None):
    if key is None:
        key = lambda x: x

    # group the elements by their key
    grouped_items = defaultdict(list)
    for item in seq_to_sort:
        k = key(item)
        grouped_items[k].append(item)

    # flatten the dict of groups to a list
    return [item for key in desired_order for item in grouped_items[key]]

# Usage:

a = [("ax", 1), ("ec", 3), ("bk", 5)]
b = ["ec", "ax", "bk"]
print(a)
print(b)
result = sorted_by(a, b, lambda tup: tup[0])
print(result)  # output: [("ec", 3), ("ax", 1), ("bk", 5)]

# Notes:

# This is a stable sort; if two list items have the same key, their order will be preserved. 
# Example:

# sorted_by([1, 2, 3], [5], key=lambda x: 5)
# [1, 2, 3]
# If any list elements are mapped to keys that don't exist in desired_order, those elements are  
# silently discarded. For example:

# sorted_by([1, 2, 3], [1, 2, 3], key=lambda x: 5)
'''