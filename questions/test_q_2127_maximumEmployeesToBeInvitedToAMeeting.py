import pytest
from q_2127_maximumEmployeesToBeInvitedToAMeeting import Solution


@pytest.mark.parametrize(
    "favorite, output", [([2, 2, 1, 2], 3), ([1, 2, 0], 3), ([3, 0, 1, 4, 1], 4)]
)
class TestSolution:
    def test_maximumInvitations(self, favorite: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumInvitations(
                favorite,
            )
            == output
        )
