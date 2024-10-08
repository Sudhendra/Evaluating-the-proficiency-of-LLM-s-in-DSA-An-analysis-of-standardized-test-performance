class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        left, right = 0, n - 1
        index = n - 1
        
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            
            if left_sq > right_sq:
                result[index] = left_sq
                left += 1
            else:
                result[index] = right_sq
                right -= 1
                
            index -= 1
        
        return result

# Time complexity: O(n)
# Space complexity: O(n)