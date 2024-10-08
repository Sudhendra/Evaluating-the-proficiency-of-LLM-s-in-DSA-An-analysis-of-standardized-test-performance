    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        cycle = False
        for i in range(n):
            next_day = [0] * 8
            for j in range(1, 7):
                if cells[j-1] == cells[j+1]:
                    next_day[j] = 1
                else:
                    next_day[j] = 0
            if tuple(next_day) in seen:
                cycle = True
                break
            seen[tuple(cells)] = i
            cells = next_day
        
        if cycle:
            remaining_days = n % i
            for _ in range(remaining_days):
                next_day = [0] * 8
                for j in range(1, 7):
                    if cells[j-1] == cells[j+1]:
                        next_day[j] = 1
                    else:
                        next_day[j] = 0
                cells = next_day
        
        return cells
