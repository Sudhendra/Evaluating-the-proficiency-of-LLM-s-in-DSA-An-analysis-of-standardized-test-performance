class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}
        for i, num in enumerate(nums):
            if num in num_to_index and abs(i - num_to_index[num]) <= k:
                return True
            num_to_index[num] = i
        return False