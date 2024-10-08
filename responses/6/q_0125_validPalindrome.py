class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        return clean_s == clean_s[::-1]
