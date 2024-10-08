class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing spaces
        if not s:
            return 0
        
        words = s.split(" ")
        for i in range(len(words) - 1, -1, -1):
            if words[i] != "":
                return len(words[i])
        
        return 0
