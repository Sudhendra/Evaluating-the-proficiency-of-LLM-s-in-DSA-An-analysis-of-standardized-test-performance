import pytest
from q_1761_minimumDegreeOfAConnectedTrioInAGraph import Solution


@pytest.mark.parametrize(
    "n, edges, output",
    [
        (6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]], 3),
        (7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]], 0),
    ],
)
class TestSolution:
    def test_minTrioDegree(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minTrioDegree(
                n,
                edges,
            )
            == output
        )
