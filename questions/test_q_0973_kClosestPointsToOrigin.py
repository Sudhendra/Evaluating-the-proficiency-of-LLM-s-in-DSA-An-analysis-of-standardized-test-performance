import pytest
from q_0973_kClosestPointsToOrigin import Solution


@pytest.mark.parametrize(
    "points, k, output",
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
class TestSolution:
    def test_kClosest(self, points: List[List[int]], k: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.kClosest(
                points,
                k,
            )
            == output
        )
