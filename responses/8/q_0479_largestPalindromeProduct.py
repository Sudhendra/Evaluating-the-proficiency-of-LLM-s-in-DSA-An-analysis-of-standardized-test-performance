class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        high = 10 ** n - 1
        low = 10 ** (n - 1)
        for i in range(high - 1, low - 1, -1):
            num = int(str(i) + str(i)[::-1])
            j = high
            while j * j >= num:
                if num % j == 0:
                    return num % 1337
                j -= 1
        return 0
