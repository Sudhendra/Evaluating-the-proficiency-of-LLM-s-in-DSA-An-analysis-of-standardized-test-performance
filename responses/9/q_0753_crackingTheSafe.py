class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_num = k ** n
        ans = "0" * n
        visited = set([ans])
        
        for i in range(total_num):
            next_str = ans[-n+1:]
            for j in range(k-1, -1, -1):
                next_pwd = next_str + str(j)
                if next_pwd not in visited:
                    visited.add(next_pwd)
                    ans += str(j)
                    break
                
        return ans
