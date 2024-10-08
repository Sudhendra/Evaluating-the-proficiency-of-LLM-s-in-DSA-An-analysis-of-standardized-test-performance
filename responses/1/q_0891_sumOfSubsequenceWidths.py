from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mod = 10**9 + 7

        ans = 0
        pow2 = [1]
        for i in range(1, n):
            pow2.append(pow2[-1]*2 % mod)

        for i in range(n):
            ans = (ans + (pow2[i] - pow2[n-i-1]) * nums[i]) % mod

        return ans
