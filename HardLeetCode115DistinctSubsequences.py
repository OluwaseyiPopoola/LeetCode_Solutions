"""
https://leetcode.com/problems/distinct-subsequences/description/?envType=daily-question&envId=2026-10-28
"""

# Final Solution: Tabulation: O(n * m) time, O(n) Space (^__^)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def explore(si, ti, s, t, memo):
            # print(si, ti)
            if (si, ti) in memo:
                return memo[(si, ti)]


            if (ti == len(t) - 1) and si < len(s) and s[si] == t[ti]:
                return 1

            if (si == len(s)) or ((si - len(s)) > (ti - len(t))) or s[si] != t[ti]:
                return 0

            cnt = 0
            for nsi in range(si + 1, len(s)):
                cnt += explore(nsi, ti + 1, s, t, memo)
                # print(si, ti, cnt)

            memo[(si, ti)] = cnt
            return memo[(si, ti)]



        if len(s) < len(t):
            return 0
        

        cnt = 0
        memo = {}
        for si in range(len(s) - len(t) + 1):
            cnt += explore(si, 0, s, t, memo)

        # print(memo)

        return cnt


# First solution: Memoization O(n**2 * m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def explore(si, ti, s, t, memo):
            # print(si, ti)
            if (si, ti) in memo:
                return memo[(si, ti)]


            if (ti == len(t) - 1) and si < len(s) and s[si] == t[ti]:
                return 1

            if (si == len(s)) or ((si - len(s)) > (ti - len(t))) or s[si] != t[ti]:
                return 0

            cnt = 0
            for nsi in range(si + 1, len(s)):
                cnt += explore(nsi, ti + 1, s, t, memo)
                # print(si, ti, cnt)

            memo[(si, ti)] = cnt
            return memo[(si, ti)]



        if len(s) < len(t):
            return 0
        

        cnt = 0
        memo = {}
        for si in range(len(s) - len(t) + 1):
            cnt += explore(si, 0, s, t, memo)

        # print(memo)

        return cnt

