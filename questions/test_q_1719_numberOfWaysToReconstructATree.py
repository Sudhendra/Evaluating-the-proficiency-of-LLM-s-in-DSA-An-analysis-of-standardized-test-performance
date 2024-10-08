import pytest
from q_1719_numberOfWaysToReconstructATree import Solution


@pytest.mark.parametrize(
    "pairs, output",
    [
        ([[1, 2], [2, 3]], 1),
        ([[1, 2], [2, 3], [1, 3]], 2),
        ([[1, 2], [2, 3], [2, 4], [1, 5]], 0),
    ],
)
class TestSolution:
    def test_checkWays(self, pairs: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.checkWays(
                pairs,
            )
            == output
        )
