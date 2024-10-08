class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_gas = 0
        start_index = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            current_gas += diff

            if current_gas < 0:
                current_gas = 0
                start_index = i + 1

        return start_index if total_gas >= 0 else -1