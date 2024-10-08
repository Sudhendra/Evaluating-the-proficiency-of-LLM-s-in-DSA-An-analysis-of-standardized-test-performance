import pytest
from q_2497_maximumStarSumOfAGraph import Solution


@pytest.mark.parametrize(
    "vals, edges, k, output",
    [
        (
            [1, 2, 3, 4, 10, -10, -20],
            [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]],
            2,
            16,
        ),
        ([-5], [], 0, -5),
    ],
)
class TestSolution:
    def test_maxStarSum(
        self, vals: List[int], edges: List[List[int]], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maxStarSum(
                vals,
                edges,
                k,
            )
            == output
        )
