import pytest
from q_2446_determineIfTwoEventsHaveConflict import Solution


@pytest.mark.parametrize(
    "event1, event2, output",
    [
        (["01:15", "02:00"], ["02:00", "03:00"], True),
        (["01:00", "02:00"], ["01:20", "03:00"], True),
        (["10:00", "11:00"], ["14:00", "15:00"], False),
    ],
)
class TestSolution:
    def test_haveConflict(self, event1: List[str], event2: List[str], output: bool):
        sc = Solution()
        assert (
            sc.haveConflict(
                event1,
                event2,
            )
            == output
        )
