import pytest
from q_3026_maximumGoodSubarraySum import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([1, 2, 3, 4, 5, 6], 1, 11), ([-1, 3, 2, 4, 5], 3, 11), ([-1, -2, -3, -4], 2, -6)],
)
class TestSolution:
    def test_maximumSubarraySum(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumSubarraySum(
                nums,
                k,
            )
            == output
        )
