import pytest
from q_2054_twoBestNonOverlappingEvents import Solution


@pytest.mark.parametrize(
    "events, output",
    [
        ([[1, 3, 2], [4, 5, 2], [2, 4, 3]], 4),
        ([[1, 3, 2], [4, 5, 2], [1, 5, 5]], 5),
        ([[1, 5, 3], [1, 5, 1], [6, 6, 5]], 8),
    ],
)
class TestSolution:
    def test_maxTwoEvents(self, events: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxTwoEvents(
                events,
            )
            == output
        )
