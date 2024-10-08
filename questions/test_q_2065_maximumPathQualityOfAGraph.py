import pytest
from q_2065_maximumPathQualityOfAGraph import Solution


@pytest.mark.parametrize(
    "values, edges, maxTime, output",
    [
        ([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49, 75),
        ([5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30, 25),
        ([1, 2, 3, 4], [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50, 7),
    ],
)
class TestSolution:
    def test_maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maximalPathQuality(
                values,
                edges,
                maxTime,
            )
            == output
        )
