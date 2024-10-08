class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = sum(shifts) % 26
        result = []
        for i, char in enumerate(s):
            shift = (ord(char) - ord('a') + total_shift) % 26
            result.append(chr(ord('a') + shift))
            total_shift = (total_shift - shifts[i]) % 26
        return "".join(result)