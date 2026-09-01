class Solution:
    def countSubstrings(self, s: str) -> int:

        count = len(s)

        for i in range(1, len(s)):
            
            start_stop = [(i - 1, i + 1), (i - 1, i)]

            for start, stop in start_stop:
                while (start >= 0 and stop < len(s)) and (s[start] == s[stop]):
                    count += 1
                    start -= 1
                    stop += 1

        return count
                  

        