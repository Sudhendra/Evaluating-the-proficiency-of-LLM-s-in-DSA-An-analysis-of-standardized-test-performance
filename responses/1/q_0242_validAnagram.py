class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        
        return s_count == t_count