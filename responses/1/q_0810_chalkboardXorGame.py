class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        xor_all = 0
        for num in nums:
            xor_all ^= num
        return xor_all == 0