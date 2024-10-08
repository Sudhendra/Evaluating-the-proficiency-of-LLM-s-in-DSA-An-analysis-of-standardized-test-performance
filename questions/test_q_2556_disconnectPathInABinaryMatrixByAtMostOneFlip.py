import pytest
from q_2556_disconnectPathInABinaryMatrixByAtMostOneFlip import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 1, 1], [1, 0, 0], [1, 1, 1]], True),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], False),
    ],
)
class TestSolution:
    def test_isPossibleToCutPath(self, grid: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.isPossibleToCutPath(
                grid,
            )
            == output
        )
