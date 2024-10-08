class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False

        n = len(nums)
        min_nums = [nums[0]]
        for i in range(1, n):
            min_nums.append(min(min_nums[-1], nums[i]))

        stack = []
        for j in range(n - 1, -1, -1):
            if nums[j] > min_nums[j]:
                while stack and stack[-1] <= min_nums[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False
