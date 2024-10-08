class Solution:
    
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        prev_person = -1
        max_distance = 0
        
        for i in range(N):
            if seats[i] == 1:
                if prev_person == -1:
                    max_distance = i
                else:
                    max_distance = max(max_distance, (i - prev_person) // 2)
                prev_person = i
                
        return max(max_distance, N - 1 - prev_person)
