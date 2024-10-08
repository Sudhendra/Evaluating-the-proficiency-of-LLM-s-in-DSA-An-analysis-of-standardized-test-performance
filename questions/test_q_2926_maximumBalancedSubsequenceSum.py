import pytest
from q_2926_maximumBalancedSubsequenceSum import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 3, 5, 6], 14), ([5, -1, -3, 8], 13), ([-2, -1], -1)]
)
class TestSolution:
    def test_maxBalancedSubsequenceSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxBalancedSubsequenceSum(
                nums,
            )
            == output
        )
