import pytest
from q_2044_countNumberOfMaximumBitwiseOrSubsets import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 1], 2), ([2, 2, 2], 7), ([3, 2, 1, 5], 6)]
)
class TestSolution:
    def test_countMaxOrSubsets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countMaxOrSubsets(
                nums,
            )
            == output
        )
