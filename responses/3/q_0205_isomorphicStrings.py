class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map_s = {}
        char_map_t = {}
        
        for i in range(len(s)):
            if s[i] in char_map_s:
                if char_map_s[s[i]] != t[i]:
                    return False
            else:
                char_map_s[s[i]] = t[i]
                
            if t[i] in char_map_t:
                if char_map_t[t[i]] != s[i]:
                    return False
            else:
                char_map_t[t[i]] = s[i]
        
        return True