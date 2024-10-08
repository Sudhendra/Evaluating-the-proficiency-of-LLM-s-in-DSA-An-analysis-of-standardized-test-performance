class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_columns_to_delete = 0
        for col in zip(*strs):
            if any(col[i] > col[i + 1] for i in range(len(col) - 1)):
                num_columns_to_delete += 1
        return num_columns_to_delete
        