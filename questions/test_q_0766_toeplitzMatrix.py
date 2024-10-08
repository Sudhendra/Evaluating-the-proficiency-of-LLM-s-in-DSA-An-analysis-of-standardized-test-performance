import pytest
from q_0766_toeplitzMatrix import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True), ([[1, 2], [2, 2]], False)],
)
class TestSolution:
    def test_isToeplitzMatrix(self, matrix: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.isToeplitzMatrix(
                matrix,
            )
            == output
        )
