from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        mem = {0: 0}
        
        for rod in rods:
            curr = mem.copy()
            for diff, height in mem.items():
                curr[diff + rod] = max(curr.get(diff + rod, 0), height)
                curr[abs(diff - rod)] = max(curr.get(abs(diff - rod), 0), height + min(diff, rod))
            
            mem = curr
        
        return mem[0]
