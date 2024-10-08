import pytest
from q_0867_transposeMatrix import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ],
)
class TestSolution:
    def test_transpose(self, matrix: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.transpose(
                matrix,
            )
            == output
        )
