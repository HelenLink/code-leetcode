"""26. Remove Duplicates from Sorted Array
Share
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
unique element appears only once. The relative order of the elements should be kept the same.
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]"""

# l - left point and unique

a = [1, 1, 2, 3, 3]
l = 1  # left point
for r in range(1, len(a)):  # r - right point
    if a[r] != a[r - 1]:
        a[l] = a[r]
        l += 1
print(l)
