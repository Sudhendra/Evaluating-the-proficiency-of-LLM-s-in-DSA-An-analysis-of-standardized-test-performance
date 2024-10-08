class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        if num <= 10 or num == 11:
            return str(num - 1)
        
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        
        def generate_palindromes(num_str):
            num = int(num_str)
            candidates = set()
            for i in [-1, 0, 1]:
                prefix = str(int(num_str[:len(num_str)//2]) + i)
                if len(num_str) % 2 == 0:
                    candidate = int(prefix + prefix[::-1])
                    candidates.add(candidate)
                else:
                    for j in [-1, 0, 1]:
                        candidate = int(prefix + str(int(num_str[len(num_str)//2]) + j) + prefix[::-1])
                        candidates.add(candidate)
            return candidates
        
        nearest_diff = float('inf')
        nearest_palindrome = None
        candidates = generate_palindromes(n)
        
        candidates.discard(num)
        for candidate in candidates:
            if abs(candidate - num) < nearest_diff:
                nearest_diff = abs(candidate - num)
                nearest_palindrome = candidate
            elif abs(candidate - num) == nearest_diff:
                nearest_palindrome = min(nearest_palindrome, candidate)
        
        return str(nearest_palindrome)