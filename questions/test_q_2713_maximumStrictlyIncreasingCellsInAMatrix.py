import pytest
from q_2713_maximumStrictlyIncreasingCellsInAMatrix import Solution


@pytest.mark.parametrize(
    "mat, output",
    [([[3, 1], [3, 4]], 2), ([[1, 1], [1, 1]], 1), ([[3, 1, 6], [-9, 5, 7]], 4)],
)
class TestSolution:
    def test_maxIncreasingCells(self, mat: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxIncreasingCells(
                mat,
            )
            == output
        )
