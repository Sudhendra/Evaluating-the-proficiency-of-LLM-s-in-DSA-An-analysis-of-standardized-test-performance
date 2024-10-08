class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return
        
        def partition(nums, low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1
        
        def find_kth_largest(nums, k):
            low, high = 0, len(nums) - 1
            while low <= high:
                pivot_idx = partition(nums, low, high)
                if pivot_idx == k:
                    return nums[pivot_idx]
                elif pivot_idx < k:
                    low = pivot_idx + 1
                else:
                    high = pivot_idx - 1
        
        middle = find_kth_largest(nums, n // 2)
        
        def map_index(i):
            return (1 + 2 * i) % (n | 1)
        
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            if nums[map_index(mid)] > middle:
                nums[map_index(low)], nums[map_index(mid)] = nums[map_index(mid)], nums[map_index(low)]
                low += 1
                mid += 1
            elif nums[map_index(mid)] < middle:
                nums[map_index(mid)], nums[map_index(high)] = nums[map_index(high)], nums[map_index(mid)]
                high -= 1
            else:
                mid += 1
