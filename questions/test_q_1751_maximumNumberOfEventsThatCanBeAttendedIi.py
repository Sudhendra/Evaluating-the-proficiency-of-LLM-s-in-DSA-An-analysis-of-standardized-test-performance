import pytest
from q_1751_maximumNumberOfEventsThatCanBeAttendedIi import Solution


@pytest.mark.parametrize(
    "events, k, output",
    [
        ([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2, 7),
        ([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2, 10),
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3, 9),
    ],
)
class TestSolution:
    def test_maxValue(self, events: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxValue(
                events,
                k,
            )
            == output
        )
