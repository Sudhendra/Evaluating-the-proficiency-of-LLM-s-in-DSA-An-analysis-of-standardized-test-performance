import pytest
from q_1870_minimumSpeedToArriveOnTime import Solution


@pytest.mark.parametrize(
    "dist, hour, output", [([1, 3, 2], 6, 1), ([1, 3, 2], 2.7, 3), ([1, 3, 2], 1.9, -1)]
)
class TestSolution:
    def test_minSpeedOnTime(self, dist: List[int], hour: float, output: int):
        sc = Solution()
        assert (
            sc.minSpeedOnTime(
                dist,
                hour,
            )
            == output
        )
