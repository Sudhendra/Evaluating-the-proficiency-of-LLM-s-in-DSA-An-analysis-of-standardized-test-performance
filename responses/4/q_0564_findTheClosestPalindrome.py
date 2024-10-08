class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def is_palindrome(num):
            return str(num) == str(num)[::-1]

        n = int(n)

        # Check for edge case when n is a single digit
        if n <= 10:
            return str(n - 1)

        # Find all possible palindrome candidates
        candidates = set()
        candidates.add(10 ** (len(str(n))) + 1)
        candidates.add(10 ** (len(str(n)) - 1) - 1)
        half = int(str(n)[:((len(str(n)) + 1) // 2)])
        for h in [half - 1, half, half + 1]:
            if len(str(n)) % 2 == 0:
                candidate = int(str(h) + str(h)[::-1])
            else:
                candidate = int(str(h) + str(h)[:-1][::-1])
            candidates.add(candidate)

        # Find the closest palindrome
        diff = float('inf')
        res = ""
        for candidate in candidates:
            if candidate != n and abs(candidate - n) < diff:
                diff = abs(candidate - n)
                res = str(candidate)
            elif candidate != n and abs(candidate - n) == diff:
                res = min(res, str(candidate))

        return res
