"""
https://leetcode.com/problems/distinct-subsequences/description/?envType=daily-question&envId=2026-10-28
"""

# Final Solution: Tabulation: O(n * m) time, O(n) Space (^__^)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        if n < m:
            return 0

        dp = [0]*n
        dp[0] = 1 if s[0] == t[0] else 0

        for i in range(1, n):
            x = 1 if s[i] == t[0] else 0
            dp[i] = dp[i - 1] + x
        
        # print(dp)

        for j in range(1, m):
            prev = None
            for i in range(j, n):
                if i == j:
                    prev = dp[i]
                    if dp[i - 1] == 1 and s[i] == t[j]:
                        dp[i] = 1
                    else:
                        dp[i] = 0

                elif s[i] != t[j]:
                    prev = dp[i]
                    dp[i] = dp[i - 1]
                
                elif s[i] == t[j]:
                    temp = dp[i]
                    dp[i] = dp[i - 1] + prev
                    prev = temp


        return dp[-1]

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

