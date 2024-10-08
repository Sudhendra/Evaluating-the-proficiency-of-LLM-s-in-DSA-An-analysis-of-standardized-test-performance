import pytest
from q_2461_maximumSumOfDistinctSubarraysWithLengthK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 5, 4, 2, 9, 9, 9], 3, 15), ([4, 4, 4], 3, 0)]
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
