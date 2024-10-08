class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        result = 0

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD

        for i in range(n):
            result = (result + (pow2[i]-pow2[n-1-i]) * nums[i]) % MOD

        return result
