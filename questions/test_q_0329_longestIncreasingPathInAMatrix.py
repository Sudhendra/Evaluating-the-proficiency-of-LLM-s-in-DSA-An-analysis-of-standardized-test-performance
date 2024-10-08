import pytest
from q_0329_longestIncreasingPathInAMatrix import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
        ([[1]], 1),
    ],
)
class TestSolution:
    def test_longestIncreasingPath(self, matrix: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.longestIncreasingPath(
                matrix,
            )
            == output
        )
