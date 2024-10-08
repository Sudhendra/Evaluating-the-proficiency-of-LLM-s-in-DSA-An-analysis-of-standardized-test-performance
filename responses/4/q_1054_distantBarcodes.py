class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        queue = []
        for num, freq in count.items():
            queue.extend([num]*freq)
        res = [0]*len(barcodes)
        res[::2], res[1::2] = queue[len(barcodes)//2:], queue[:len(barcodes)//2]
        return res
