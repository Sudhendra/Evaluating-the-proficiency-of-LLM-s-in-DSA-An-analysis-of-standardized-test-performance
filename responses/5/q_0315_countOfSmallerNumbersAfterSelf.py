class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(arr, start, end, smaller_counts):
            if start >= end:
                return
            mid = start + (end - start) // 2
            merge_sort(arr, start, mid, smaller_counts)
            merge_sort(arr, mid + 1, end, smaller_counts)
            merge(arr, start, mid, end, smaller_counts)

        def merge(arr, start, mid, end, smaller_counts):
            merged = []
            left, right = start, mid + 1
            right_count = 0
            while left <= mid and right <= end:
                if arr[right][1] < arr[left][1]:
                    right_count += 1
                    merged.append(arr[right])
                    right += 1
                else:
                    smaller_counts[arr[left][0]] += right_count
                    merged.append(arr[left])
                    left += 1

            while left <= mid:
                smaller_counts[arr[left][0]] += right_count
                merged.append(arr[left])
                left += 1

            while right <= end:
                merged.append(arr[right])
                right += 1

            for i in range(len(merged)):
                arr[start + i] = merged[i]

        n = len(nums)
        result = [0] * n
        indexed_nums = [(i, num) for i, num in enumerate(nums)]
        merge_sort(indexed_nums, 0, n - 1, result)

        return result