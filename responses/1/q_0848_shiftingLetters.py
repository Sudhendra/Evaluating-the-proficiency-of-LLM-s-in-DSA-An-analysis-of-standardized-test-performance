class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = sum(shifts) % 26
        result = []
        
        for i in range(len(s)):
            shifted_char = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))
            result.append(shifted_char)
            total_shift = (total_shift - shifts[i]) % 26
        
        return ''.join(result)