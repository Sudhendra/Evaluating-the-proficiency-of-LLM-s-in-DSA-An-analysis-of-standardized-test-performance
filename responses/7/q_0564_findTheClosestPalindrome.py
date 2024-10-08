class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        half = n[:(length+1)//2]  # Get the first half of the number
        
        # Generate palindromes based on the first half of the number
        candidates = set()
        candidates.add(str(10 ** length + 1))  # Upper bound
        candidates.add(str(10 ** (length - 1) - 1))  # Lower bound
        # Palindrome formed by just the first half
        candidates.add(half + half[::-1][:length % 2])
        # Palindromes by incrementing and decrementing the first half by 1 while preserving the first digit
        candidates.add(str(int(half) - 1) + (str(int(half) - 1)[::-1])[:length % 2])
        candidates.add(str(int(half) + 1) + (str(int(half) + 1)[::-1])[:length % 2])
        
        num = int(n)
        diff = float('inf')  # Initialize minimum absolute difference
        closest_palindrome = ''
        
        for candidate in candidates:
            candidate_num = int(candidate)
            if candidate_num == num:
                continue  # Skip the same number
                
            if abs(candidate_num - num) < diff or (abs(candidate_num - num) == diff and candidate_num < int(closest_palindrome)):
                diff = abs(candidate_num - num)
                closest_palindrome = candidate
        
        return closest_palindrome
