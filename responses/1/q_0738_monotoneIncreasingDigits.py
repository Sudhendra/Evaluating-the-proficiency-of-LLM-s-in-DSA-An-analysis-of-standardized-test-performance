class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num_str = list(str(n))
        length = len(num_str)
        
        j = length
        for i in range(length-1, 0, -1):
            if num_str[i] < num_str[i-1]:
                num_str[i-1] = str(int(num_str[i-1]) - 1)
                j = i
        
        for i in range(j, length):
            num_str[i] = '9'
        
        return int("".join(num_str))