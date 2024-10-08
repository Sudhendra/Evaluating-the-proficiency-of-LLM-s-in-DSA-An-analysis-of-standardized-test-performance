class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Convert integer to binary representation
        binary_representation = bin(n)[2:]
        
        # Check if the binary representation has alternating bits
        for i in range(1, len(binary_representation)):
            if binary_representation[i] == binary_representation[i - 1]:
                return False
        
        return True