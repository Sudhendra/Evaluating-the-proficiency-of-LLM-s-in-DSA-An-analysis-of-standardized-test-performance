class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_digits = k ** n
        ans = "0" * n
        visited = set()
        
        while len(ans) < total_digits:
            for i in range(k-1, -1, -1):
                new_ans = ans[(len(ans)-n+1):] + str(i)
                if new_ans not in visited:
                    visited.add(new_ans)
                    ans += str(i)
                    break
        
        return ans