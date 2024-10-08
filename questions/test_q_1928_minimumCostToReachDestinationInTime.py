import pytest
from q_1928_minimumCostToReachDestinationInTime import Solution


@pytest.mark.parametrize(
    "maxTime, edges, passingFees, output",
    [
        (
            30,
            [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
            [5, 1, 2, 20, 20, 3],
            11,
        ),
        (
            29,
            [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
            [5, 1, 2, 20, 20, 3],
            48,
        ),
        (
            25,
            [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
            [5, 1, 2, 20, 20, 3],
            -1,
        ),
    ],
)
class TestSolution:
    def test_minCost(
        self, maxTime: int, edges: List[List[int]], passingFees: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.minCost(
                maxTime,
                edges,
                passingFees,
            )
            == output
        )
