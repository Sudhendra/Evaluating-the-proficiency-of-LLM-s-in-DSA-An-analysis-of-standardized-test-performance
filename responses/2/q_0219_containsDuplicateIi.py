class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index_map = {}
        for i, num in enumerate(nums):
            if num in num_index_map and i - num_index_map[num] <= k:
                return True
            num_index_map[num] = i
        return False