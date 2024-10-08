import pytest
from q_0073_setMatrixZeroes import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
    ],
)
class TestSolution:
    def test_setZeroes(self, matrix: List[List[int]], output: None):
        sc = Solution()
        assert (
            sc.setZeroes(
                matrix,
            )
            == output
        )
