from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        
        def backtrack(curr_str, i):
            if i == len(s):
                result.append(curr_str)
                return
            
            if s[i].isalpha():
                backtrack(curr_str + s[i].lower(), i+1)
                backtrack(curr_str + s[i].upper(), i+1)
            else:
                backtrack(curr_str + s[i], i+1)
        
        backtrack("", 0)
        
        return result