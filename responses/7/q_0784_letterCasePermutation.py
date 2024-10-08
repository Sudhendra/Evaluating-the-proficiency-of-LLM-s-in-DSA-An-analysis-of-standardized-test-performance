from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.dfs(s, "", res)
        return res
    
    def dfs(self, s, curr, res):
        if not s:
            res.append(curr)
            return
        
        if s[0].isalpha():
            self.dfs(s[1:], curr + s[0].lower(), res)
            self.dfs(s[1:], curr + s[0].upper(), res)
        else:
            self.dfs(s[1:], curr + s[0], res)
