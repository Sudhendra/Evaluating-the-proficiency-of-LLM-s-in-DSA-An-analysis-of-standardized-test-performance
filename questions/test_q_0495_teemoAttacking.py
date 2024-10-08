import pytest
from q_0495_teemoAttacking import Solution


@pytest.mark.parametrize(
    "timeSeries, duration, output", [([1, 4], 2, 4), ([1, 2], 2, 3)]
)
class TestSolution:
    def test_findPoisonedDuration(
        self, timeSeries: List[int], duration: int, output: int
    ):
        sc = Solution()
        assert (
            sc.findPoisonedDuration(
                timeSeries,
                duration,
            )
            == output
        )
