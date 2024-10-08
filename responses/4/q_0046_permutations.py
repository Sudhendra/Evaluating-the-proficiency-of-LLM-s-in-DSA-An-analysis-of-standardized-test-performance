class Solution:
    def permute(self, nums):
        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        result = []
        backtrack([])
        return result