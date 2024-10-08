class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = sum(shift % 26 for shift in shifts) % 26
        shifted = []
        for i, c in enumerate(s):
            shift = ord(c) - ord('a') + total_shift
            new_char = chr(ord('a') + shift % 26)
            shifted.append(new_char)
            total_shift -= shifts[i] % 26
        return ''.join(shifted)
