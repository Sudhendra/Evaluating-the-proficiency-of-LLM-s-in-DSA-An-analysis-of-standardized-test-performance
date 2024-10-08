class Solution:
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        diag_dict = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                diag_dict[i+j].append(mat[i][j])

        result = []
        
        for key in diag_dict.keys():
            if key % 2 == 0:
                result.extend(reversed(diag_dict[key]))
            else:
                result.extend(diag_dict[key])
        
        return result
