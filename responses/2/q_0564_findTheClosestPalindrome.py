class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == '1':
            return '0'
        
        def is_palindrome(num):
            return num == num[::-1]
        
        length = len(n)
        candidates = set()
        candidates.add('9' * (length - 1))
        candidates.add('1' + '0' * (length - 1) + '1')
        
        prefix = int(n[:(length + 1)//2])
        for i in range(-1, 2):
            num = str(prefix + i)
            candidates.add(num + num[::-1][:length // 2])  # Even length palindrome
            candidates.add(num + num[::-1][:(length - 1) // 2])  # Odd length palindrome

        n_int = int(n)
        min_diff = float('inf')
        result = None
        
        for candidate in candidates:
            candidate_int = int(candidate)
            if candidate_int != n_int:
                diff = abs(candidate_int - n_int)
                if diff < min_diff or (diff == min_diff and candidate_int < int(result)):
                    min_diff = diff
                    result = candidate
        
        return result