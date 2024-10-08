class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        s_ptr = 0
        t_ptr = 0
        
        while t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                if s_ptr == len(s):
                    return True
            t_ptr += 1
        
        return False