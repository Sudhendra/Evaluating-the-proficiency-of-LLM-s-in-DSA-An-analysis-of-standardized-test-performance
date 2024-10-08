from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed.append(0)  # Adding extra '0' at the end to cover edge case
        i = 0
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                count += 1
                i += 2  # Skip the next space as it can't have a flower
            else:
                i += 1
        return count >= n
