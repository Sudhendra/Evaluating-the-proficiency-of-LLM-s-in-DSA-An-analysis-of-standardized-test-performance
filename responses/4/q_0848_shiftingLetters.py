from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = sum(shift % 26 for shift in shifts) % 26
        result = []
        for i, char in enumerate(s):
            shift = (ord(char) - ord('a') + total_shift) % 26
            new_char = chr(ord('a') + shift)
            result.append(new_char)
            total_shift = (total_shift - shifts[i]) % 26
        return ''.join(result)
