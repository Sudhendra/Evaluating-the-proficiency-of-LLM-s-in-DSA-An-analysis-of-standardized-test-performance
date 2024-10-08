from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = sum(shifts) % 26
        result = []
        for i, char in enumerate(s):
            shift = total_shift % 26
            new_char_val = ord(char) + shift
            if new_char_val > ord('z'):
                new_char_val -= 26
            result.append(chr(new_char_val))
            total_shift -= shifts[i]
        return "".join(result)
