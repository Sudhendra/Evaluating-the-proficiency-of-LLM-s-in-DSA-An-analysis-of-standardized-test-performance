import pytest
from q_1360_numberOfDaysBetweenTwoDates import Solution


@pytest.mark.parametrize(
    "date1, date2, output",
    [("2019-06-29", "2019-06-30", 1), ("2020-01-15", "2019-12-31", 15)],
)
class TestSolution:
    def test_daysBetweenDates(self, date1: str, date2: str, output: int):
        sc = Solution()
        assert (
            sc.daysBetweenDates(
                date1,
                date2,
            )
            == output
        )
