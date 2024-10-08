class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        if sx == tx and sy <= ty and (ty - sy) % sx == 0:
            return True
        if sy == ty and sx <= tx and (tx - sx) % sy == 0:
            return True
        return sx == tx and sy == ty
