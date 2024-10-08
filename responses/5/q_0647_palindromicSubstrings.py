class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def count_palindromes(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            count_palindromes(i, i)  # odd length palindromes
            count_palindromes(i, i + 1)  # even length palindromes

        return count