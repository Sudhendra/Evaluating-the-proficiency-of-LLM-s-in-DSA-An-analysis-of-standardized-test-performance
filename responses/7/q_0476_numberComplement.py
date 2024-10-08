class Solution:
    def findComplement(self, num: int) -> int:
        x = 1
        while num >= x:
            x = x * 2
        return num ^ (x - 1)
