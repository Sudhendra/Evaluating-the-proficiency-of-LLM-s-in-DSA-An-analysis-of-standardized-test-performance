from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = sum(shift % 26 for shift in shifts) % 26
        result = []
        for i, char in enumerate(s):
            new_ascii = ord(char) + total_shift
            if new_ascii > ord('z'):
                new_ascii -= 26
            result.append(chr(new_ascii))
            total_shift = (total_shift - shifts[i]) % 26
        return ''.join(result)
