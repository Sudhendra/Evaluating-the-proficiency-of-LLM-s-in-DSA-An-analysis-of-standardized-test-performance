class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        
        for a in range(upper - 1, lower - 1, -1):
            num = int(str(a) + str(a)[::-1])
            
            for b in range(upper, lower - 1, -1):
                if num // b > upper:
                    break
                if num % b == 0:
                    return num % 1337

        return -1  # This line is reached only if the loop above doesn't find a solution

