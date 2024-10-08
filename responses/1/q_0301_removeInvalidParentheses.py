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
        
        def dfs(s, start, left_removed, right_removed, left_count, right_count, path, result):
            if start == len(s):
                if left_removed == 0 and right_removed == 0 and is_valid(path):
                    result.add(path)
                return
            
            if s[start] == '(' and left_removed > 0:
                dfs(s, start+1, left_removed-1, right_removed, left_count, right_count, path, result)
            elif s[start] == ')' and right_removed > 0:
                dfs(s, start+1, left_removed, right_removed-1, left_count, right_count, path, result)
            
            path += s[start]

            if s[start] != '(' and s[start] != ')':
                dfs(s, start+1, left_removed, right_removed, left_count, right_count, path, result)
            elif s[start] == '(':
                dfs(s, start+1, left_removed, right_removed, left_count+1, right_count, path, result)
            elif right_count < left_count:
                dfs(s, start+1, left_removed, right_removed, left_count, right_count+1, path, result)
            
            path = path[:-1]
        
        left_removed, right_removed = 0, 0
        for char in s:
            if char == '(':
                left_removed += 1
            elif char == ')':
                if left_removed == 0:
                    right_removed += 1
                else:
                    left_removed -= 1
        
        result = set()
        dfs(s, 0, left_removed, right_removed, 0, 0, "", result)
        return list(result)
