import pytest
from q_3025_findTheNumberOfWaysToPlacePeopleI import Solution


@pytest.mark.parametrize(
    "points, output",
    [
        ([[1, 1], [2, 2], [3, 3]], 0),
        ([[6, 2], [4, 4], [2, 6]], 2),
        ([[3, 1], [1, 3], [1, 1]], 2),
    ],
)
class TestSolution:
    def test_numberOfPairs(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numberOfPairs(
                points,
            )
            == output
        )
