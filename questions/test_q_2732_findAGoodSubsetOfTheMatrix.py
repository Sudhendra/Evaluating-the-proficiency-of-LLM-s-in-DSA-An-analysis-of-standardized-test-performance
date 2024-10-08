import pytest
from q_2732_findAGoodSubsetOfTheMatrix import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]], [0, 1]),
        ([[0]], [0]),
        ([[1, 1, 1], [1, 1, 1]], []),
    ],
)
class TestSolution:
    def test_goodSubsetofBinaryMatrix(self, grid: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.goodSubsetofBinaryMatrix(
                grid,
            )
            == output
        )
