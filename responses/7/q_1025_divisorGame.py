class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

# Test the solution
solution = Solution()
print(solution.divisorGame(2))  # Output: true
print(solution.divisorGame(3))  # Output: false
