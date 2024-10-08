import pytest
from q_0327_countOfRangeSum import Solution


@pytest.mark.parametrize(
    "nums, lower, upper, output", [([-2, 5, -1], -2, 2, 3), ([0], 0, 0, 1)]
)
class TestSolution:
    def test_countRangeSum(self, nums: List[int], lower: int, upper: int, output: int):
        sc = Solution()
        assert (
            sc.countRangeSum(
                nums,
                lower,
                upper,
            )
            == output
        )
