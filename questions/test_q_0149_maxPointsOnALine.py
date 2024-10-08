import pytest
from q_0149_maxPointsOnALine import Solution


@pytest.mark.parametrize(
    "points, output",
    [
        ([[1, 1], [2, 2], [3, 3]], 3),
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
    ],
)
class TestSolution:
    def test_maxPoints(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxPoints(
                points,
            )
            == output
        )
