class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        upper = 10**n - 1
        lower = (upper + 1) // 10
        
        for i in range(upper, lower - 1, -1):
            palindrome = int(str(i) + str(i)[::-1])
            j = upper
            while j * j >= palindrome:
                if palindrome % j == 0:
                    return palindrome % 1337
                j -= 1
        return -1
