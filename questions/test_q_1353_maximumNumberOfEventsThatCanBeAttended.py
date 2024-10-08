import pytest
from q_1353_maximumNumberOfEventsThatCanBeAttended import Solution


@pytest.mark.parametrize(
    "events, output",
    [([[1, 2], [2, 3], [3, 4]], 3), ([[1, 2], [2, 3], [3, 4], [1, 2]], 4)],
)
class TestSolution:
    def test_maxEvents(self, events: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxEvents(
                events,
            )
            == output
        )
