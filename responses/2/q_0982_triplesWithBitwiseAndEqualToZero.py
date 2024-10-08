class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = [0] * (1 << 16)
        for i in range(len(nums)):
            for j in range(1 << 16):
                if j & nums[i] == 0:
                    count[j] += 1
        result = 0
        for i in range(1 << 16):
            for j in range(len(nums)):
                if nums[j] & i == 0:
                    result += count[i]
        return result