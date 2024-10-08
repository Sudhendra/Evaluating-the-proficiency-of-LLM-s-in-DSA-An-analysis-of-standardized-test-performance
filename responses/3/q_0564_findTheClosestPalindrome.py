class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == '1':
            return '0'
        num = int(n)
        small_palindrome = palindrome_helper(num, -1)
        big_palindrome = palindrome_helper(num, 1)
        return str(small_palindrome) if abs(small_palindrome - num) <= abs(big_palindrome - num) else str(big_palindrome)

def palindrome_helper(num, change):
    num_str = str(num)
    length = len(num_str)
    half_len = (length + 1) // 2
    left_half = int(num_str[:(length - 1) // 2 + 1])
    
    left_half += change
    if change < 0 or len(str(left_half)) < len(str(num)) // 2:
        return int(str(left_half) + str(left_half)[:-1][::-1])
    else:
        return int(str(left_half) + str(left_half)[:-1 if length % 2 == 0 else None][::-1])