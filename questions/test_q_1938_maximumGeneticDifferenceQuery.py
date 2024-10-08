import pytest
from q_1938_maximumGeneticDifferenceQuery import Solution


@pytest.mark.parametrize(
    "parents, queries, output",
    [
        ([-1, 0, 1, 1], [[0, 2], [3, 2], [2, 5]], [2, 3, 7]),
        ([3, 7, -1, 2, 0, 7, 0, 2], [[4, 6], [1, 15], [0, 5]], [6, 14, 7]),
    ],
)
class TestSolution:
    def test_maxGeneticDifference(
        self, parents: List[int], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.maxGeneticDifference(
                parents,
                queries,
            )
            == output
        )
