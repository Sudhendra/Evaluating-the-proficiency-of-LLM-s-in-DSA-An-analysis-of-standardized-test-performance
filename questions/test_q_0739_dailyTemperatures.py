import pytest
from q_0739_dailyTemperatures import Solution


@pytest.mark.parametrize(
    "temperatures, output",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ],
)
class TestSolution:
    def test_dailyTemperatures(self, temperatures: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.dailyTemperatures(
                temperatures,
            )
            == output
        )
