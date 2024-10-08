class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        max_num = 10**n - 1
        min_num = 10**(n-1)
        for a in range(max_num, min_num-1, -1):
            palindrome = int(str(a) + str(a)[::-1])
            for b in range(max_num, int(palindrome ** 0.5) - 1, -1):
                if palindrome % b == 0:
                    return palindrome % 1337
        return -1