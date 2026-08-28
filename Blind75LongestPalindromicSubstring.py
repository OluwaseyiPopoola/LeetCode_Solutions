"""
for all i where 0 < i < len(s) - 1

at index i
    pos_palindromic paths

    if s[i] == s[i - 1]







"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        long_start = long_stop = 0
        for i in range(1, len(s)):

            pos_start_stop = [(i - 1, i + 1), (i - 1, i)]
            for start, stop in pos_start_stop:
                
                found = False
                while (start >= 0 and stop < len(s)) and s[start] == s[stop]:

                    found = True
                    start -= 1
                    stop += 1

                start += 1
                stop -= 1

                if found and stop - start > long_stop - long_start:
                    long_start = start
                    long_stop = stop


        return s[long_start: long_stop + 1]
            