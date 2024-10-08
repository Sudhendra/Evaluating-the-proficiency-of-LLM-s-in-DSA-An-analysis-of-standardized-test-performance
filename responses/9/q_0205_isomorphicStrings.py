class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        mapping_s = {}
        mapping_t = {}
        
        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s:
                mapping_s[char_s] = char_t
            if char_t not in mapping_t:
                mapping_t[char_t] = char_s
            if mapping_s[char_s] != char_t or mapping_t[char_t] != char_s:
                return False
        
        return True
