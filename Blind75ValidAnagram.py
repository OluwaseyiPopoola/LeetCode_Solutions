"""
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_freq = {}

        for char in s:
            if char not in s_char_freq:
                s_char_freq[char] = 0
            s_char_freq[char] += 1

        for char in t:
            if char not in s_char_freq:
                return False

            s_char_freq[char] -= 1
            if s_char_freq[char] == 0:
                del s_char_freq[char]

        return not s_char_freq
            
        
                  

        