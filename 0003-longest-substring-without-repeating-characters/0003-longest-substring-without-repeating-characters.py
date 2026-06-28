class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        ans = 1
        set1 = set()
        set1.add(s[0])

        i = 0
        j = 1
         
        while j < n:
            # If a duplicate is found, shrink the window from the left
            while s[j] in set1:
                set1.discard(s[i])
                i += 1  # FIX 1: Increment i to avoid an infinite loop

            # Add the current character to the set
            set1.add(s[j])
            j += 1
            
            # FIX 2: Correctly calculate the current window length (j - i)
            ans = max(ans, j - i)

        return ans