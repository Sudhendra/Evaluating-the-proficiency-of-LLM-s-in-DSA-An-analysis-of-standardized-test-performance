import pytest
from q_1770_maximumScoreFromPerformingMultiplicationOperations import Solution


@pytest.mark.parametrize(
    "nums, multipliers, output",
    [([1, 2, 3], [3, 2, 1], 14), ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102)],
)
class TestSolution:
    def test_maximumScore(self, nums: List[int], multipliers: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumScore(
                nums,
                multipliers,
            )
            == output
        )
