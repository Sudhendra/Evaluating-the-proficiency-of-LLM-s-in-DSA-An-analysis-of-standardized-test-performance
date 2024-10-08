import pytest
from q_1072_flipColumnsForMaximumNumberOfEqualRows import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[0, 1], [1, 1]], 1),
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2),
    ],
)
class TestSolution:
    def test_maxEqualRowsAfterFlips(self, matrix: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxEqualRowsAfterFlips(
                matrix,
            )
            == output
        )
