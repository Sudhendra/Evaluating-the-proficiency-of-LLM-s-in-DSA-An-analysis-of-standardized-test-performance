class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = collections.defaultdict(list)
        tails = collections.defaultdict(int)
        
        for num in nums:
            if freq[num - 1]:
                prev_length = heapq.heappop(freq[num - 1])
                heapq.heappush(freq[num], prev_length + 1)
                
                if prev_length == 2:
                    tails[num] += 1
            else:
                heapq.heappush(freq[num], 1)
                
        for tail in tails.values():
            if tail < 3:
                return False
        
        return True