"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        """"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]"""

nums = [3, 4, 5, 6, 10]
target = int(input())

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
