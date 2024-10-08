from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr_gas = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]
            
            if curr_gas < 0:
                start_index = i + 1
                curr_gas = 0
        
        return start_index if total_gas >= 0 else -1
