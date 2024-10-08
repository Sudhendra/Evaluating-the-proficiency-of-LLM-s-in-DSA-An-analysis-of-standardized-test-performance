import pytest
from q_2172_maximumAndSumOfArray import Solution


@pytest.mark.parametrize(
    "nums, numSlots, output", [([1, 2, 3, 4, 5, 6], 3, 9), ([1, 3, 10, 4, 7, 1], 9, 24)]
)
class TestSolution:
    def test_maximumANDSum(self, nums: List[int], numSlots: int, output: int):
        sc = Solution()
        assert (
            sc.maximumANDSum(
                nums,
                numSlots,
            )
            == output
        )
