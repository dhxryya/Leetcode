class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0] * (n +1)

        for x in arr:
            cnt[min(x,n)] +=1

        val = 0 

        for i in range(1,n+1):
            val = min(i, val + cnt[i]) 

        return val     