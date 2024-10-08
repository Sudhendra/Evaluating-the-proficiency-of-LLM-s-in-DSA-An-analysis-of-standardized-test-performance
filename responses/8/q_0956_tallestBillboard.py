from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        memo = {0: 0}

        for rod in rods:
            curr_memo = memo.copy()
            for diff, height in memo.items():
                memo[diff + rod] = max(memo.get(diff + rod, 0), height)
                memo[abs(diff - rod)] = max(memo.get(abs(diff - rod), 0), height + min(diff, rod))
        
        return memo[0]

# Test cases
solution = Solution()
print(solution.tallestBillboard([1, 2, 3, 6]))  # Output: 6
print(solution.tallestBillboard([1, 2, 3, 4, 5, 6]))  # Output: 10
print(solution.tallestBillboard([1, 2]))  # Output: 0
