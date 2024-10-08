class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        freq = [0] * (1 << 16)

        for i in range(n):
            for j in range(n):
                freq[nums[i] & nums[j]] += 1

        for k in range(n):
            for f in freq:
                if nums[k] & f == 0:
                    count += f

        return count