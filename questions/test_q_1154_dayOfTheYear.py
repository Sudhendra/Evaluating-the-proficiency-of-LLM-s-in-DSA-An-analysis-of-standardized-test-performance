import pytest
from q_1154_dayOfTheYear import Solution


@pytest.mark.parametrize("date, output", [("2019-01-09", 9), ("2019-02-10", 41)])
class TestSolution:
    def test_dayOfYear(self, date: str, output: int):
        sc = Solution()
        assert (
            sc.dayOfYear(
                date,
            )
            == output
        )
