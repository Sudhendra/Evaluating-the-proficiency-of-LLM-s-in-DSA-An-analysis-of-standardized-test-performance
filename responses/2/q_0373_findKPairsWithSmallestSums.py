class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        minHeap = []
        
        for i in range(min(k, len(nums1))):
            # Add pair (num1, num2, index of num2)
            heapq.heappush(minHeap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        
        result = []
        
        while k > 0 and minHeap:
            _, num1, num2, index2 = heapq.heappop(minHeap)
            result.append([num1, num2])
            k -= 1
            
            if index2 + 1 < len(nums2):
                next_sum = num1 + nums2[index2 + 1]
                heapq.heappush(minHeap, (next_sum, num1, nums2[index2 + 1], index2 + 1))
        
        return result