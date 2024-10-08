class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        result = 0
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % mod

        for i in range(n):
            result = (result + (pow2[i] - pow2[n - 1 - i]) * nums[i]) % mod

        return result
