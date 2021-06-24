# Compute Intersection
# Given two arrays, write a function to compute their intersection.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique

def join(arr1, arr2):
    newlist = set([x for x in arr1 if x in arr2])
    print(newlist)

def oneline(arr1, arr2):
    print(list(set([x for x in arr1 if x in arr2])))

join([1,2,2,1], [2,2])

oneline([4,9,5], [9,4,9,8,4])