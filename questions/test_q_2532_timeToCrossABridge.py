import pytest
from q_2532_timeToCrossABridge import Solution


@pytest.mark.parametrize(
    "n, k, time, output",
    [
        (1, 3, [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]], 6),
        (3, 2, [[1, 9, 1, 8], [10, 10, 10, 10]], 50),
    ],
)
class TestSolution:
    def test_findCrossingTime(self, n: int, k: int, time: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findCrossingTime(
                n,
                k,
                time,
            )
            == output
        )
