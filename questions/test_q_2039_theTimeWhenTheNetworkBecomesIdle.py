import pytest
from q_2039_theTimeWhenTheNetworkBecomesIdle import Solution


@pytest.mark.parametrize(
    "edges, patience, output",
    [([[0, 1], [1, 2]], [0, 2, 1], 8), ([[0, 1], [0, 2], [1, 2]], [0, 10, 10], 3)],
)
class TestSolution:
    def test_networkBecomesIdle(
        self, edges: List[List[int]], patience: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.networkBecomesIdle(
                edges,
                patience,
            )
            == output
        )
