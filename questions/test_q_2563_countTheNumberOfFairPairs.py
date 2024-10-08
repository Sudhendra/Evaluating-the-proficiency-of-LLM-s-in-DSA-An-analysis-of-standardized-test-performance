import pytest
from q_2563_countTheNumberOfFairPairs import Solution


@pytest.mark.parametrize(
    "nums, lower, upper, output",
    [([0, 1, 7, 4, 4, 5], 3, 6, 6), ([1, 7, 9, 2, 5], 11, 11, 1)],
)
class TestSolution:
    def test_countFairPairs(self, nums: List[int], lower: int, upper: int, output: int):
        sc = Solution()
        assert (
            sc.countFairPairs(
                nums,
                lower,
                upper,
            )
            == output
        )
