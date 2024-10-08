from collections import Counter

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_num = max(nums)
        count = Counter(nums)
        moves = 0
        
        for i in range(max_num + 1):
            while count[i] > 1:
                for j in range(i + 1, max_num + 2):
                    if count[j] == 0:
                        count[j] += 1
                        moves += j - i
                        count[i] -= 1
                        break
        
        return moves
