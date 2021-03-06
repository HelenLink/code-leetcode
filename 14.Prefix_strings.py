"""14. Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""


def longest(strs):
    a = ''
    for i in zip(*strs):

        if len(set(i)) == 1:
            a += i[0]
        else:
            break
    return a
