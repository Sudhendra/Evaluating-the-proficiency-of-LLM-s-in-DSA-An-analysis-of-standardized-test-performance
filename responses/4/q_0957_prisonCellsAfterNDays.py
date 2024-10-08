class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cycle = {}
        state = cells.copy()
        for day in range(n):
            state_tuple = tuple(state)
            if state_tuple in cycle:
                remaining_days = n - day
                remaining_cycles = remaining_days % (day - cycle[state_tuple])
                return cycle_list[remaining_cycles - 1]
            else:
                new_state = [0] * 8
                for i in range(1, 7):
                    new_state[i] = 1 if state[i-1] == state[i+1] else 0
                cycle[state_tuple] = day
                state = new_state
        
        return state
