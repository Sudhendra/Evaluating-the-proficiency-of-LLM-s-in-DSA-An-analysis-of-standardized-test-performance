import pytest
from q_0688_knightProbabilityInChessboard import Solution


@pytest.mark.parametrize(
    "n, k, row, column, output", [(3, 2, 0, 0, 0.0625), (1, 0, 0, 0, 1.0)]
)
class TestSolution:
    def test_knightProbability(
        self, n: int, k: int, row: int, column: int, output: float
    ):
        sc = Solution()
        assert (
            sc.knightProbability(
                n,
                k,
                row,
                column,
            )
            == output
        )
