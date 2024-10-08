from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False

        target_sum = total_sum // 3  # Calculate the target sum for each part
        current_sum, count = 0, 0

        for num in arr:
            current_sum += num
            if current_sum == target_sum:
                count += 1
                current_sum = 0  # Reset the current sum to start calculating for the next part

        return count >= 3

# Example usage:
solution = Solution()
arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
print(solution.canThreePartsEqualSum(arr))  # Output: True
