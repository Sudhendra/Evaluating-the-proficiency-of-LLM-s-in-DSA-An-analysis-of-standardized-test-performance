import pytest
from q_2467_mostProfitablePathInATree import Solution


@pytest.mark.parametrize(
    "edges, bob, amount, output",
    [
        ([[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6], 6),
        ([[0, 1]], 1, [-7280, 2350], -7280),
    ],
)
class TestSolution:
    def test_mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.mostProfitablePath(
                edges,
                bob,
                amount,
            )
            == output
        )
