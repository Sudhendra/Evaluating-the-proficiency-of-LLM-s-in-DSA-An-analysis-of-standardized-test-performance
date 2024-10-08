import pytest
from q_1735_countWaysToMakeArrayWithProduct import Solution


@pytest.mark.parametrize(
    "queries, output",
    [
        ([[2, 6], [5, 1], [73, 660]], [4, 1, 50734910]),
        ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [1, 2, 3, 10, 5]),
    ],
)
class TestSolution:
    def test_waysToFillArray(self, queries: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.waysToFillArray(
                queries,
            )
            == output
        )
