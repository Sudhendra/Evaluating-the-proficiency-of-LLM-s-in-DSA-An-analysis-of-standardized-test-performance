class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n+1):
            binary_i = bin(i)[2:]  # Get binary representation of current number i
            if binary_i not in s:  # Check if binary_i is substring of s
                return False
        return True
