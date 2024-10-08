class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            row.reverse()
            for i in range(n):
                row[i] = 1 - row[i]
        return image