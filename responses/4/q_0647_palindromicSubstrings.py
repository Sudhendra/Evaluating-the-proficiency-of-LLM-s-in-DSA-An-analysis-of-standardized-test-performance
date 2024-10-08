class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindromes(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0
        for i in range(len(s)):
            total_palindromes += count_palindromes(i, i)  # Odd length palindromes
            total_palindromes += count_palindromes(i, i + 1)  # Even length palindromes

        return total_palindromes
