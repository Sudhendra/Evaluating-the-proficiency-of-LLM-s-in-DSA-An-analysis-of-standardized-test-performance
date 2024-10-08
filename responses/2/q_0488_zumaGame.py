from collections import Counter

class Solution:
    
    def findMinStep(self, board: str, hand: str) -> int:
        def dfs(balls):
            if not balls: return 0
            res = float('inf')
            i = 0
            while i < len(balls):
                start = i
                while i < len(balls) and balls[i] == balls[start]:
                    i += 1
                need = 3 - (i - start)
                if counter[balls[start]] >= need:
                    need = max(0, need)
                    counter[balls[start]] -= need
                    prev, balls = balls[:start], balls[i:]
                    new_balls = prev + balls
                    while new_balls and new_balls[0] == balls[start]:
                        new_balls = balls[start] + new_balls
                    res = min(res, need + dfs(new_balls))
                    counter[balls[start]] += need
            return res
        
        counter = Counter(hand)
        result = dfs(board)
        return -1 if result == float('inf') else result if result < 6 else -1
