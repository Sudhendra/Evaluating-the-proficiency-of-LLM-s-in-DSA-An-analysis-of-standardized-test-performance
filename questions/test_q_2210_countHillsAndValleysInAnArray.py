import pytest
from q_2210_countHillsAndValleysInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 4, 1, 1, 6, 5], 3), ([6, 6, 5, 5, 4, 1], 0)]
)
class TestSolution:
    def test_countHillValley(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countHillValley(
                nums,
            )
            == output
        )
