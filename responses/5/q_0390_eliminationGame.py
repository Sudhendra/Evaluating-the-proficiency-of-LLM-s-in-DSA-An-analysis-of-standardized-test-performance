class Solution:
    def lastRemaining(self, n: int) -> int:
        # Helper function to calculate remaining numbers after each elimination
        def remaining(n, left_to_right):
            if n == 1:
                return 1
            if left_to_right:
                return 2 * remaining(n // 2, not left_to_right)
            else:
                if n % 2 == 0:
                    return 2 * remaining(n // 2, not left_to_right) - 1
                else:
                    return 2 * remaining(n // 2, not left_to_right)
        
        return remaining(n, True)
