class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Initializing the search space
        
        while left < right:
            mid = left + (right - left) // 2  # Calculating the middle version

            if isBadVersion(mid):  # Checking if the middle version is bad
                right = mid  # Setting the right boundary to mid
            else:
                left = mid + 1  # Setting the left boundary to mid + 1
        
        return left  # Returning the first bad version