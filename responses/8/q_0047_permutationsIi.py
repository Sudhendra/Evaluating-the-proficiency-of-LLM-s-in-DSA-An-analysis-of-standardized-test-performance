from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, counter):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[num] += 1
        
        result = []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        backtrack([], counter)
        return result

solution = Solution()
print(solution.permuteUnique([1, 1, 2]))  # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
print(solution.permuteUnique([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
