class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned_str == cleaned_str[::-1]