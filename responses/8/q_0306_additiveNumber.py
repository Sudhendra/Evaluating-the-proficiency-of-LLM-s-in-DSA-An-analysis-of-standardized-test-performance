class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(num, path):
            if not num and len(path) >= 3:
                return True
            for i in range(1, len(num) + 1):
                if i > 1 and num[0] == '0':
                    continue
                if len(path) < 2 or int(num[:i]) == path[-1] + path[-2]:
                    if dfs(num[i:], path + [int(num[:i])]):
                        return True
            return False
        
        return dfs(num, [])
