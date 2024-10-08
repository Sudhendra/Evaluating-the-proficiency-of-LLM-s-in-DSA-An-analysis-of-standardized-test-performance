class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        result = ""
        for i in range(len(s)):
            shift = shifts[i] % 26
            result += chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))

        return result