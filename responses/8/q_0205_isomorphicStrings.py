    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping_st = {}
        mapping_ts = {}
        
        for char_s, char_t in zip(s, t):
            if char_s not in mapping_st:
                mapping_st[char_s] = char_t
            if char_t not in mapping_ts:
                mapping_ts[char_t] = char_s
            
            if mapping_st[char_s] != char_t or mapping_ts[char_t] != char_s:
                return False
        
        return True
