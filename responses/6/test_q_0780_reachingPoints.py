import pytest
from q_0780_reachingPoints import Solution


@pytest.mark.parametrize(
    "sx, sy, tx, ty, output",
    [(1, 1, 3, 5, True), (1, 1, 2, 2, False), (1, 1, 1, 1, True)],
)
class TestSolution:
    def test_reachingPoints(self, sx: int, sy: int, tx: int, ty: int, output: bool):
        sc = Solution()
        assert (
            sc.reachingPoints(
                sx,
                sy,
                tx,
                ty,
            )
            == output
        )
