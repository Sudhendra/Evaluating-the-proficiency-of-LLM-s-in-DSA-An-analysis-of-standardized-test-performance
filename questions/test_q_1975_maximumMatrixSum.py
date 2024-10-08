import pytest
from q_1975_maximumMatrixSum import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [([[1, -1], [-1, 1]], 4), ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16)],
)
class TestSolution:
    def test_maxMatrixSum(self, matrix: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxMatrixSum(
                matrix,
            )
            == output
        )
