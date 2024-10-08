import pytest
from q_1904_theNumberOfFullRoundsYouHavePlayed import Solution


@pytest.mark.parametrize(
    "loginTime, logoutTime, output", [("09:31", "10:14", 1), ("21:30", "03:00", 22)]
)
class TestSolution:
    def test_numberOfRounds(self, loginTime: str, logoutTime: str, output: int):
        sc = Solution()
        assert (
            sc.numberOfRounds(
                loginTime,
                logoutTime,
            )
            == output
        )
