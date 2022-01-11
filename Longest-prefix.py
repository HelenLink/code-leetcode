"""14. Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

strs = ["flower", "flow", "flight"]


def devide(strs):
    if len(strs) is None or len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    s = ''
    mid = len(strs) // 2
    left = devide(strs[:mid])
    right = devide(strs[mid:])
    for i, j in zip(left, right):
        print(i, j)
        if i != j:
            break
        s += i
    return s
