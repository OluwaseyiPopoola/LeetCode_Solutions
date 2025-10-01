"""
Problem: https://leetcode.com/problems/longest-common-prefix?envType=problem-list-v2&envId=array

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

Thought Process:

Brute Force:
- if first element == "": return "" # Handle Edge case of looping through empty string
-  Loop through the chars of the first_string
-  Loop through the remaining strings
-  Compare them to the chars of other elements at the same position
-  When not equal to char at same positon or position not exist, first_string[:i]
-  If loops finishes: return first_string
"""



class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs[0] == "":
            return ""
        