class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespaces
        if " " not in s:  # If there is no space remaining, return the length of the entire string
            return len(s)
        else:
            return len(s.split()[-1])  # Split the string by space and return the length of the last element
