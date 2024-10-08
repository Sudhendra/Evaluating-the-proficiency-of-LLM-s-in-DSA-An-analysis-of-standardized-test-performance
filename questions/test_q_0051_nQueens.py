import pytest
from q_0051_nQueens import Solution


@pytest.mark.parametrize(
    "n, output",
    [
        (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
        (1, [["Q"]]),
    ],
)
class TestSolution:
    def test_solveNQueens(self, n: int, output: List[List[str]]):
        sc = Solution()
        assert (
            sc.solveNQueens(
                n,
            )
            == output
        )
