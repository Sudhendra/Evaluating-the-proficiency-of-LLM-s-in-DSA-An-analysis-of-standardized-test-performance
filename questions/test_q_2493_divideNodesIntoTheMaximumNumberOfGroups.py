import pytest
from q_2493_divideNodesIntoTheMaximumNumberOfGroups import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (6, [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]], 4),
        (3, [[1, 2], [2, 3], [3, 1]], -1),
    ],
)
class TestSolution:
    def test_magnificentSets(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.magnificentSets(
                n,
                edges,
            )
            == output
        )
