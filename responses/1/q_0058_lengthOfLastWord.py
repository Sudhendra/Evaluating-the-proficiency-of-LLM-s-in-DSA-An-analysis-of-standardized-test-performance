class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespaces
        if ' ' not in s:  # If there are no spaces, return the length of the whole string
            return len(s)
        return len(s.split()[-1])  # Split the string by spaces and return the length of the last word
