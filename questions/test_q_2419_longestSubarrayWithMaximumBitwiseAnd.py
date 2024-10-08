import pytest
from q_2419_longestSubarrayWithMaximumBitwiseAnd import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3, 3, 2, 2], 2), ([1, 2, 3, 4], 1)])
class TestSolution:
    def test_longestSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestSubarray(
                nums,
            )
            == output
        )
