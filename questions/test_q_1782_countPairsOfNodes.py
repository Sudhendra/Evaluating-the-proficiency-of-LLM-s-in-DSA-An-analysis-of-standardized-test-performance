import pytest
from q_1782_countPairsOfNodes import Solution


@pytest.mark.parametrize(
    "n, edges, queries, output",
    [
        (4, [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], [2, 3], [6, 5]),
        (
            5,
            [[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]],
            [1, 2, 3, 4, 5],
            [10, 10, 9, 8, 6],
        ),
    ],
)
class TestSolution:
    def test_countPairs(
        self, n: int, edges: List[List[int]], queries: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.countPairs(
                n,
                edges,
                queries,
            )
            == output
        )
