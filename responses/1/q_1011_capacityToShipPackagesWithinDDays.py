class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            curr_sum = 0
            required_days = 1
            
            for weight in weights:
                curr_sum += weight
                if curr_sum > mid:
                    curr_sum = weight
                    required_days += 1
            
            if required_days <= days:
                right = mid
            else:
                left = mid + 1
                
        return left
