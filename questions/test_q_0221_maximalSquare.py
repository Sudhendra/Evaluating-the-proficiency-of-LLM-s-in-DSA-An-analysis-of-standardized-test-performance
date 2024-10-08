import pytest
from q_0221_maximalSquare import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
        ([["0", "1"], ["1", "0"]], 1),
        ([["0"]], 0),
    ],
)
class TestSolution:
    def test_maximalSquare(self, matrix: List[List[str]], output: int):
        sc = Solution()
        assert (
            sc.maximalSquare(
                matrix,
            )
            == output
        )
