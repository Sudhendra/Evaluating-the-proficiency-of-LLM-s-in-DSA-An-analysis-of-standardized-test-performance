class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        max_num = 10 ** n - 1
        min_num = 10 ** (n - 1)
        
        for a in range(max_num, min_num - 1, -1):
            palin = int(str(a) + str(a)[::-1])
            for b in range(max_num, int((palin)**0.5) - 1, -1):
                if palin % b == 0 and palin // b <= max_num:
                    return palin % 1337