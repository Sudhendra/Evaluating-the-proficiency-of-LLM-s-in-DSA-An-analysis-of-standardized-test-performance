import pytest
from q_3033_modifyTheMatrix import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[1, 2, -1], [4, -1, 6], [7, 8, 9]], [[1, 2, 9], [4, 8, 6], [7, 8, 9]]),
        ([[3, -1], [5, 2]], [[3, 2], [5, 2]]),
    ],
)
class TestSolution:
    def test_modifiedMatrix(self, matrix: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.modifiedMatrix(
                matrix,
            )
            == output
        )
