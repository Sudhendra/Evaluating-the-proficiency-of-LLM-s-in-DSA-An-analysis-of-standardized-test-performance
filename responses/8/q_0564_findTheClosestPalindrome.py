class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def is_palindrome(x):
            return x == x[::-1]

        n = int(n)
        if n < 10:
            return str(n - 1)

        def generate_palindrome(length, first_half):
            second_half = first_half[::-1]
            if length % 2 == 0:
                return int(first_half + second_half)
            else:
                return int(first_half + second_half[1:])

        length = len(n)
        candidates = set([str(10**length - 1), str(10**length + 1), str(10**(length-1) - 1)])
        first_half = n[:(length + 1) // 2]
        for prefix in map(str, [int(first_half) - 1, int(first_half), int(first_half) + 1]):
            candidates.add(str(generate_palindrome(length, prefix)))
        candidates.discard(str(n))

        closest = None
        min_diff = float('inf')
        for candidate in candidates:
            diff = abs(int(candidate) - n)
            if diff < min_diff or (diff == min_diff and int(candidate) < int(closest)):
                closest = candidate
                min_diff = diff

        return closest
