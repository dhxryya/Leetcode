class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        # Change range(i, n-2) to range(n-2) or range(0, n-2)
        for i in range(n - 2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i+2] != s[i]:
                ans += 1
                
        return ans