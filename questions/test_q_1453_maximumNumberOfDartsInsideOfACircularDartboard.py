import pytest
from q_1453_maximumNumberOfDartsInsideOfACircularDartboard import Solution


@pytest.mark.parametrize(
    "darts, r, output",
    [
        ([[-2, 0], [2, 0], [0, 2], [0, -2]], 2, 4),
        ([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5, 5),
    ],
)
class TestSolution:
    def test_numPoints(self, darts: List[List[int]], r: int, output: int):
        sc = Solution()
        assert (
            sc.numPoints(
                darts,
                r,
            )
            == output
        )
