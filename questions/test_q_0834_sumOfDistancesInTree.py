import pytest
from q_0834_sumOfDistancesInTree import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]], [8, 12, 6, 10, 10, 10]),
        (1, [], [0]),
        (2, [[1, 0]], [1, 1]),
    ],
)
class TestSolution:
    def test_sumOfDistancesInTree(
        self, n: int, edges: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.sumOfDistancesInTree(
                n,
                edges,
            )
            == output
        )
