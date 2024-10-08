import pytest
from q_2501_longestSquareStreakInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 3, 6, 16, 8, 2], 3), ([2, 3, 5, 6, 7], -1)]
)
class TestSolution:
    def test_longestSquareStreak(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestSquareStreak(
                nums,
            )
            == output
        )
