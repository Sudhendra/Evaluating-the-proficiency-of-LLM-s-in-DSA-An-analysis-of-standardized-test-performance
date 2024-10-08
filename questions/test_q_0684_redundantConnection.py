import pytest
from q_0684_redundantConnection import Solution


@pytest.mark.parametrize(
    "edges, output",
    [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ],
)
class TestSolution:
    def test_findRedundantConnection(self, edges: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.findRedundantConnection(
                edges,
            )
            == output
        )
