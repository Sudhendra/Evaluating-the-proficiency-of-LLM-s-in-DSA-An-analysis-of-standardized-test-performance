class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        
        if num == 0 or num == 1:
            return True
        
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            mid_squared = mid * mid
            if mid_squared == num:
                return True
            elif mid_squared < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False