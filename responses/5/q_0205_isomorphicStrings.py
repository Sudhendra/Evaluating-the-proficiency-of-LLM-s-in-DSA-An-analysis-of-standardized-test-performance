class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping_s_t = {}
        mapping_t_s = {}
        
        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s_t:
                mapping_s_t[char_s] = char_t
            else:
                if mapping_s_t[char_s] != char_t:
                    return False
                
            if char_t not in mapping_t_s:
                mapping_t_s[char_t] = char_s
            else:
                if mapping_t_s[char_t] != char_s:
                    return False
        
        return True