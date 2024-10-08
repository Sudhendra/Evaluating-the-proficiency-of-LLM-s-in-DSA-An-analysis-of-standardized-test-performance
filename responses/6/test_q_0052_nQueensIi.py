import pytest
from q_0052_nQueensIi import Solution


@pytest.mark.parametrize("n, output", [(4, 2), (1, 1)])
class TestSolution:
    def test_totalNQueens(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.totalNQueens(
                n,
            )
            == output
        )
