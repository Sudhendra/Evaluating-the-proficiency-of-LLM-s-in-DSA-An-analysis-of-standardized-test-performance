class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        min_left = [0] * n
        stack = []
        
        min_left[0] = nums[0]
        for i in range(1, n):
            min_left[i] = min(min_left[i-1], nums[i])
        
        for j in range(n-1, -1, -1):
            if nums[j] > min_left[j]:
                while stack and stack[-1] <= min_left[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False