import pytest
from q_0825_friendsOfAppropriateAges import Solution


@pytest.mark.parametrize(
    "ages, output", [([16, 16], 2), ([16, 17, 18], 2), ([20, 30, 100, 110, 120], 3)]
)
class TestSolution:
    def test_numFriendRequests(self, ages: List[int], output: int):
        sc = Solution()
        assert (
            sc.numFriendRequests(
                ages,
            )
            == output
        )
