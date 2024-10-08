from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        def backtrack(s, start, left_removed, right_removed, left_count, right_count, path, result):
            if left_count < 0 or right_count < 0:
                return
            if start == len(s):
                if left_removed == 0 and right_removed == 0 and is_valid(path):
                    result.add(path)
                return
            
            if s[start] == '(':
                backtrack(s, start+1, left_removed-1, right_removed, left_count, right_count, path, result)
                backtrack(s, start+1, left_removed, right_removed, left_count+1, right_count, path+'(', result)
            elif s[start] == ')':
                backtrack(s, start+1, left_removed, right_removed-1, left_count, right_count, path, result)
                backtrack(s, start+1, left_removed, right_removed, left_count, right_count+1, path+')', result)
            else:
                backtrack(s, start+1, left_removed, right_removed, left_count, right_count, path+s[start], result)
        
        left_removed = 0
        right_removed = 0
        for char in s:
            if char == '(':
                left_removed += 1
            elif char == ')':
                if left_removed == 0:
                    right_removed += 1
                else:
                    left_removed -= 1
        
        result = set()
        backtrack(s, 0, left_removed, right_removed, 0, 0, '', result)
        return list(result)