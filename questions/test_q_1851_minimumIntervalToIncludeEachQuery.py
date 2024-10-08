import pytest
from q_1851_minimumIntervalToIncludeEachQuery import Solution


@pytest.mark.parametrize(
    "intervals, queries, output",
    [
        ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),
        ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22], [2, -1, 4, 6]),
    ],
)
class TestSolution:
    def test_minInterval(
        self, intervals: List[List[int]], queries: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.minInterval(
                intervals,
                queries,
            )
            == output
        )
