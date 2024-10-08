class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mod = 10**9 + 7
        res = 0
        powers_of_2 = [1]
        for i in range(1, n):
            powers_of_2.append((powers_of_2[-1] * 2) % mod)
        
        for i in range(n):
            res = (res + (powers_of_2[i] - powers_of_2[n-1-i]) * nums[i]) % mod

        return res
