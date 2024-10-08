class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i

        return total == num

# Example usage:
solution = Solution()
print(solution.checkPerfectNumber(28))  # Output: True
print(solution.checkPerfectNumber(7))   # Output: False
