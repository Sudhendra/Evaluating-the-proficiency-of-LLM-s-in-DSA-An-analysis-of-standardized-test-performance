class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_mapping = {}
        t_mapping = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in s_mapping:
                if s_mapping[char_s] != char_t:
                    return False
            else:
                s_mapping[char_s] = char_t
            
            if char_t in t_mapping:
                if t_mapping[char_t] != char_s:
                    return False
            else:
                t_mapping[char_t] = char_s
        
        return True