"""35. Search Insert Position
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where
it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1"""

nums = [1, 3, 5, 6]
target = 5


def binary_s(nums, item):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if nums[mid] == item:
            return mid
        if nums[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(binary_s(nums, target))
