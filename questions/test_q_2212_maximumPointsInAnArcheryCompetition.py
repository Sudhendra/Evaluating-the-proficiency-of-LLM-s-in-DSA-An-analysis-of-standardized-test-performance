import pytest
from q_2212_maximumPointsInAnArcheryCompetition import Solution


@pytest.mark.parametrize(
    "numArrows, aliceArrows, output",
    [
        (9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0], [0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1]),
        (3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]),
    ],
)
class TestSolution:
    def test_maximumBobPoints(
        self, numArrows: int, aliceArrows: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.maximumBobPoints(
                numArrows,
                aliceArrows,
            )
            == output
        )
