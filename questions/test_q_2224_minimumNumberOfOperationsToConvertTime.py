import pytest
from q_2224_minimumNumberOfOperationsToConvertTime import Solution


@pytest.mark.parametrize(
    "current, correct, output", [("02:30", "04:35", 3), ("11:00", "11:01", 1)]
)
class TestSolution:
    def test_convertTime(self, current: str, correct: str, output: int):
        sc = Solution()
        assert (
            sc.convertTime(
                current,
                correct,
            )
            == output
        )
