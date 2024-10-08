import pytest
from q_1380_luckyNumbersInAMatrix import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
        ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
        ([[7, 8], [1, 2]], [7]),
    ],
)
class TestSolution:
    def test_luckyNumbers(self, matrix: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.luckyNumbers(
                matrix,
            )
            == output
        )
