import pytest
from q_1749_maximumAbsoluteSumOfAnySubarray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, -3, 2, 3, -4], 5), ([2, -5, 1, -4, 3, -2], 8)]
)
class TestSolution:
    def test_maxAbsoluteSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxAbsoluteSum(
                nums,
            )
            == output
        )
