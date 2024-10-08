class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26  # We will assume only lowercase English letters
        
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        for char in t:
            char_count[ord(char) - ord('a')] -= 1
            if char_count[ord(char) - ord('a')] < 0:
                return False
        
        return True