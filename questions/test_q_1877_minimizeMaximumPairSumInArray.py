import pytest
from q_1877_minimizeMaximumPairSumInArray import Solution


@pytest.mark.parametrize("nums, output", [([3, 5, 2, 3], 7), ([3, 5, 4, 2, 4, 6], 8)])
class TestSolution:
    def test_minPairSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minPairSum(
                nums,
            )
            == output
        )
